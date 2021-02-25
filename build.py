import datetime
import re
import shutil
import time
import zipfile
import json
import hashlib
import nsist
import os
import logging
import subprocess
import argparse
import sys
import traceback

version = '1.0.1'
appname = "UAutoIDE"
with open(os.path.join("miniperf", "__init__.py"), encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)
    # for github action
    tag = os.getenv('tag')
    if tag and tag.startswith("refs/tags/v"):
        version = tag.replace("refs/tags/v", "")
    else:
        # add version
        x_y_z = [int(x) for x in version.split('.')]
        x_y_z[-1] += 1
        version = '.'.join(str(x) for x in x_y_z)

with open(os.path.join("miniperf", "__init__.py"), 'w', encoding="utf8") as f:
    f.write(f'__version__ = "{version}"')

tasks = {}


def task(name, depends):
    def inner_task(func):
        # print("register_task, name=%s" % (name))
        tasks[name] = [func, depends]

        def wrap(*largs, **kwargs):
            return func(*largs, **kwargs)

        return wrap

    return inner_task


def get_configs_file_name(ctx):
    """
    configs.ini
    configs_internal_debug.ini
    configs_internal_release.ini
    configs_internal_prerelease.ini
    configs_public_debug.ini
    configs_public_release.ini
    configs_public_prerelease.ini
    """
    build_type = ctx['build_type']
    flavor = ctx['flavor']
    return "configs_%s_%s.ini" % (flavor, build_type)


def get_release_file_name(ctx):
    build_type = ctx['build_type']
    flavor = ctx['flavor']
    if build_type == "release" and flavor == "public":
        return f"{appname}-{version}.zip"  # eg: UAutoIDE-v1.0.0.zip
    else:
        return "%s-%s-%s-%s.zip" % (
        appname, version, flavor, build_type)  # eg: PywebTableConvertTool-v1.0.0-internal-debug.zip


def build_ui(ctx):
    print("Task: Build UI")
    pass  # TODO: cd miniperf/ui; yarn package
    print("Task: Build UI done")


def build_wheel(ctx):
    print("Task: Build Wheel")
    subprocess.check_call(['python', 'setup.py', 'bdist', 'bdist_wheel'])

    for filename in os.listdir('src'):
        subprocess.check_call(['python', 'setup.py', 'bdist', 'bdist_wheel', '-d', '../../dist/'], cwd=f'src/{filename}')
    print("Task: Build Wheel done")


def build_nsis(ctx):
    print("Task: Build NSIS")
    icon = r'miniperf/ui/res/img/icon.ico'
    no_wheels = [
        "adb",
        "mmgui",
        "SQLAlchemy",
        "openpyxl",
        "et-xmlfile",
        "ifaddr",
        "uiautomator2"
    ]

    def req_wheel(x):
        if x.startswith('-e'):
            return False
        for nw in no_wheels:
            if nw in x:
                return False
        return True

    requirements = list(filter(req_wheel, open('requirements.txt').read().strip().split('\n')))
    wheels = list(map(lambda y: os.path.join('dist', y),
                      filter(lambda x: x.endswith('whl'), os.listdir('dist'))))
    name = "app"
    print('---------', wheels)
    builder = nsist.InstallerBuilder(
        appname=name,
        version=version,
        icon=icon,
        shortcuts={
            name: {
                'entry_point': 'miniperf.app:main',
                'console': False,
                'icon': icon,
            }
        },
        py_version='3.7.0',
        py_bitness=64,
        pypi_wheel_reqs=requirements,
        packages=[

        ],
        local_wheels=wheels,
        extra_files=[
            (get_configs_file_name(ctx), ''),
        ]
    )

    builder.run(makensis=False)
    # input("press any key to continue")
    builder.run_nsis()
    print("Task: Build NSIS done")


def zip_dir(dir_name, output_file, excludes=None):
    zip_file = zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED)
    # ziph is zipfile handle
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            file_full_path = os.path.join(root, file)
            file_rel_path = os.path.relpath(file_full_path, dir_name)
            include = True
            if excludes:
                for exclude in excludes:
                    # print("file_rel_path=%s exclude=%s" % (file_rel_path, exclude.replace("/", os.path.sep)))
                    if exclude.replace("/", os.path.sep) in file_rel_path:
                        include = False
                        continue
            if include:
                zip_file.write(file_full_path, file_rel_path)
                print("package file %s" % file_rel_path)
    zip_file.close()


def md5(filename):
    # BUF_SIZE is totally arbitrary, change for your app!
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
    hash = hashlib.md5()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            hash.update(data)
    return hash.hexdigest()


def build_package(ctx):
    print("Task: Build Package")
    nsis_dir = os.path.join(".", "build", "nsis")
    out_dir = os.path.join(".", "dist")

    # rename configs.internal.ini to configs.ini
    configs_file = os.path.join(nsis_dir, get_configs_file_name(ctx))
    if not os.path.exists(configs_file):
        print("Configs file %s is missing." % configs_file)
        sys.exit(-1)
    os.rename(configs_file, os.path.join(nsis_dir, "configs.ini"))

    release_file_name = get_release_file_name(ctx)
    release_zip_file = os.path.join(out_dir, release_file_name)
    shutil.copyfile("Main.exe", os.path.join(nsis_dir, f"{appname}.exe"))
    shutil.copyfile("LICENSE", os.path.join(nsis_dir, "LICENSE"))
    shutil.copyfile("run.bat", os.path.join(nsis_dir, "run.bat"))
    shutil.copyfile("run.sh", os.path.join(nsis_dir, "run.sh"))

    zip_dir(nsis_dir, release_zip_file, excludes=["msvcrt", "installer.nsi", "app_%s.exe" % version])

    checksum = md5(release_zip_file)
    release_date = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime())

    release_json_file = os.path.join(out_dir, "latest.json")
    release_info = {
        "version": version,
        "path": release_file_name,
        "md5": checksum,
        "releaseDate": release_date,
    }
    with open(release_json_file, "w") as f:
        json.dump(release_info, f, indent=2)
    print("Output file: %s" % release_zip_file)
    print("Task: Build Package done")


@task(name="help", depends=[])
def task_help():
    global tasks
    print("Usage: build [task_name]")
    for task_name in tasks:
        print("\tTask: %s" % task_name)
    return True


@task(name="clean", depends=[])
def clean():
    print("Task: Clean")
    build_dir = os.path.join(".", "build")
    shutil.rmtree(build_dir, ignore_errors=True)
    dist_dir = os.path.join(".", "dist")
    shutil.rmtree(dist_dir, ignore_errors=True)
    print(f"Delete dir: {build_dir} and {dist_dir}")
    return True


@task(name="debug", depends=[])
def build_debug():
    FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)

    """
    Build Type(打包版本)：
        * debug: 调试版本
        * release: 发布版本
        * prerelease: 预发布版本
    Project Flavor(产品变种):
        * internal: 内部版本(DSP账户系统，内网服务器，提供给内部测中用户使用)
        * public: 外部版本(Testplus账户系统，外网服务器，提供给外部用户使用)
    """
    # argparser = argparse.ArgumentParser()
    # argparser.add_argument("--build_type", default="release", choices=["debug", "pre-release", "release"], help="Build Type")
    # argparser.add_argument("--flavor", default="internal", choices=["internal", "public"], help="Project Flavor")
    # args = argparser.parse_args()

    ctx = {
        "build_type": "release",
        "flavor": "internal"
    }

    print("Building...")
    clean()
    build_ui(ctx)
    build_wheel(ctx)
    build_nsis(ctx)
    build_package(ctx)
    print("Build Success.")
    return True


def execute_task(task_name):
    global tasks
    task_func, depends = tasks[task_name] if task_name in tasks else None
    if not task_func:
        print("Error: `%s` task is not exists!" % task_name)
    if depends:
        for depend_task_name in depends:
            if not execute_task(depend_task_name):
                return False
    result = False
    print("------------------------------------")
    print("Execute Task: %s\n" % task_name)
    try:
        result = task_func()
    except:
        traceback.print_exc()
    print("\nExecute Task: %s, Result: %s" % (task_name, ("Success" if result else "Fail")))
    print("------------------------------------")
    return result


def main():
    task_name = "debug"  # default build debug version
    if len(sys.argv) > 1:
        task_name = sys.argv[1]

    print("--- TPT Build System ----")
    print("Target Task: `%s`" % task_name)
    result = execute_task(task_name)
    print("Build Result: %s" % ("Success" if result else "Fail"))


if __name__ == "__main__":
    main()
