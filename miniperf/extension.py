import importlib
import json
import logging
import os
import time
import traceback
import sys
import configparser
import webview
import re

from miniperf import helper, adb_helper
# from miniperf.adb import Device
from miniperf.adb import Device

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

python_path = os.path.join(os.path.split(sys.executable)[0], "python.exe")

configPath = os.path.abspath(os.path.join(".", "configs.ini"))
# configPath = os.path.join(ROOT_DIR,os.path.pardir, 'configs.ini')

config = configparser.ConfigParser()
config.read(configPath, encoding='UTF-8')

g_webview = None
phone = Device(ROOT_DIR)
isNotChanged = True
workSpacePath = config.get('Setting', 'cases_path')
if workSpacePath == r'\\':
    workSpacePath = os.path.join(ROOT_DIR, 'asset', 'WorkSpace')
sys.path.append(os.path.join(workSpacePath))
disconnected =False

class Header(object):
    def __init__(self, _comment, _filed, _type, _subtype):
        print("__HEADER__", _comment, _filed, _type, _subtype)
        _map = {"int": "0", "string": ""}
        self.Comment = _comment.replace("\n", '')
        self.Filed = _filed
        self.FiledType = _type
        self.Default = _map.get(self.FiledType, "")
        self.SubType = _subtype


def test():
    module = sys.modules['phase_Login']
    module.AutoRun(phone.device)
    return {"ok": True, "msg": '运行完成'}

def isDevicesChange():
    global isNotChanged
    while isNotChanged:
        time.sleep(0.2)
    isNotChanged = True
    return {"ok": True}

# 刷新json文件
def refreshCasesJSON():
    file_list = []
    casesList = []
    initList = []
    dir_list = os.listdir(os.path.join(workSpacePath, 'pages'))  

    for dirs in dir_list:   # 添加__init__文件
        if dirs != "__init__.py" and not os.path.isdir(os.path.join(workSpacePath, 'pages', dirs)):
            dirs = dirs.split('.')[0]
            names = "from pages import " + dirs + "\n"
            initList.append(names)

    with open(os.path.join(workSpacePath, 'pages', '__init__.py'), 'w+', encoding='UTF-8') as f:
        for i in initList:
            f.write(i)

    dir_list = os.listdir(os.path.join(workSpacePath, 'pages'))  

    if dir_list:
        for file in dir_list:   # 移除文件夹
            if os.path.isdir(os.path.join(workSpacePath, 'pages',file)):
                # dir_list.remove(file)
                continue
            else:
                file = file.split('.')[0]
                if file != '__init__' and file != '':
                    file_list.append(file)

    with open(os.path.join(workSpacePath, 'setting.UAUTO'), 'r', encoding='UTF-8') as f:
        try:
            s = json.loads(f.read())
            
            while i in range(len(file_list)):
                for value in s:
                    if file_list[i] == value['run_case']:
                        newData = {
                                "test_name": value['test_name'],
                                "tag": value['tag'],
                                "run_case": value['run_case'],
                        }
                        casesList.append(newData)
                        file_list.remove(file_list[i])

        except json.decoder.JSONDecodeError:
            if file_list != '':
                while i in range(len(file_list)):
                    newData = {
                            "test_name": file_list[i],
                            "tag": file_list[i],
                            "run_case": file_list[i],
                    }
                    casesList.append(newData)
                    file_list.remove(file_list[i])

    if file_list:
        for file in file_list:
            newData = {
                    "test_name": file,
                    "tag": file,
                    "run_case": file,
            }
            casesList.append(newData)       

    with open(os.path.join(workSpacePath, 'setting.UAUTO'), 'w', encoding='UTF-8') as f:
        json.dump(casesList, f, ensure_ascii=False)   
             
# 加载本地脚本列表
def loadCasesList():
    refreshCasesJSON()
    case_list = []
    file_list = []
    casesList = []

    with open(os.path.join(workSpacePath, 'setting.UAUTO'), 'r', encoding='UTF-8') as f:
        try:
            s = json.loads(f.read())
            for case in s:
                case = case['run_case'] + ".py"
                case_list.append(case)

            sort_list = sorted(case_list,key = lambda x: os.path.getmtime(os.path.join(workSpacePath,'pages',x))) # 按文件最后修改时间排序
            sort_list = sort_list[::-1]

            for i in sort_list:
                i = i.split('.')[0]
                file_list.append(i)

            for file in file_list:
                for value in s:
                    if file == value['run_case']:
                        # if file not in casesList['run_case']:
                        newData = {
                                "test_name": value['test_name'],
                                "tag": value['tag'],
                                "run_case": value['run_case'],
                            }
                        casesList.append(newData)
        
        except json.decoder.JSONDecodeError:
            newData = {
                "test_name": '',
                "tag": '',
                "run_case":'',
            }
            casesList.append(newData)
    
    return {"ok": True, "msg": casesList}

# 加载指定名称脚本
def loadCase(data):
    try:
        path = os.path.join(workSpacePath, 'pages', data['caseName'] + '.py')
        with open(path, 'r', encoding='UTF-8') as f:
            return {"ok": True, "msg": f.read()}
    except Exception as e:
        err_string = str(e).replace('\n','')
        print(f'[ERROR]{err_string}')
        logging.error(e)
        return {"ok": False, "msg": e}

# 打开工作区
def openUAUTOFile():
    try:
        # window = tk.Tk()
        # window.withdraw()
        # FilePath = filedialog.askopenfilename(title = "请选择项目的UAUTO文件",filetypes=[('UAUTO','*.UAUTO')],initialdir=workSpacePath)
        # FilePath = os.path.dirname(FilePath)

        FilePath = ""
        window = g_webview
        file_types = ('UAUTO (*.UAUTO)', 'All files (*.*)')        
        FilePath = window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=False, file_types=file_types)
        if FilePath != None:
            result = ''.join(FilePath[0])
            FilePath = os.path.dirname(result)
        # print(FilePath)

        if FilePath:
            data = {'path':FilePath}
            setWorkSpace(data)
            # window.destroy()
            print(FilePath + "工作区打开成功")
            return {"ok": True, "msg": FilePath + "工作区打开成功"}
        else:
            # window.destroy()
            print("已取消工作区打开")
            return ""

    except Exception as e:
        err_string = str(e).replace('\n','')
        print(f'[ERROR]{err_string}')
        # window.destroy()
        print(f'[ERROR]' + FilePath + '工作区打开失败')
        return {"ok": False, "msg": FilePath + "工作区打开失败"}

# 新建工作区
def createuserWorkSpace():
    try:
        # window = tk.Tk()
        # window.withdraw()
        # FilePath = filedialog.askdirectory(title = "请选择创建工作区的目录",initialdir=workSpacePath)

        FilePath = ""
        window = g_webview       
        FilePath = window.create_file_dialog(webview.FOLDER_DIALOG,directory=workSpacePath)
        if FilePath != None:
            FilePath = ''.join(FilePath[0])
        # print(FilePath)
        if FilePath:
            data = {'path':FilePath}
            setCreateWorkSpace(data)
            # window.destroy()
            print(FilePath +'工作区创建成功')
            # print("可通过新建脚本功能添加脚本")
            return {"ok": True, "msg": FilePath +'工作区创建成功'}
        else:
            # window.destroy()
            print("已取消工作区创建")
            return ""
            
    except Exception as e:
        err_string = str(e).replace('\n','')
        print(f'[ERROR]{err_string}')
        # window.destroy()
        print(f'[ERROR]' + FilePath + '工作区创建失败')
        return {"ok": False, "msg": FilePath + "工作区创建失败"}

# 新建工作区文件
def setCreateWorkSpace(data):
    global workSpacePath
    if not os.path.exists(os.path.join(data['path'], '*.UAUTO')):
        if os.listdir(data['path']):
            return {"ok": False, "msg": '选择的创建路径不为空'}
        else:
            createWorkSpace(data['path'])
            setWorkSpace(data)
    else:
        workSpacePath = data['path']
        # setConfig('Setting', 'cases_path', workSpacePath)
        setWorkSpace(data)
        sys.path.append(os.path.join(workSpacePath))

# 加载工作区
def setWorkSpace(data):
    global workSpacePath
    workSpacePath = data['path']
    setConfig('Setting', 'cases_path', workSpacePath)
    sys.path.append(os.path.join(workSpacePath))
    return {"ok": True, "msg": '设置成功'}

def initWorkSpace():
    # path = os.path.join(workSpacePath, 'pages')
    path = r'\\10.11.86.64\share\nginx\jx1\pages'
    print(os.path.abspath(path))
    sys.path.append(path)
    list = scan_files(path, postfix='.py')
    for script in list:
        # print()
        LoadModuleByPath(script.split('\\')[-1].split('.')[0], script)


def create(path, name, type, default=''):
    with open(os.path.join(path, name + '.' + type), 'w') as f:
        f.write(default)
        f.close()

def create1(path, name, type, default=''):
    with open(os.path.join(path, name + '.' + type), 'w+') as f:
        f.write(default)
        f.close()


# 新建工作区
def createWorkSpace(path: str):
    global workSpacePath
    try:
        workSpacePath = path
        if not os.path.exists(workSpacePath):
            os.mkdir(workSpacePath)
        os.mkdir(os.path.join(workSpacePath, 'pages'))
        create(workSpacePath, 'setting', 'UAUTO', '[]')
        create(os.path.join(workSpacePath, 'pages'), 'temp_test', 'py')
        create(os.path.join(workSpacePath, 'pages'), '__init__', 'py')
        return {"ok": True, "msg": 'ok'}
    except:
        raise "创建工作区失败"

# 新建脚本
def createFile(data):
    global workSpacePath
    try:
        pattern = re.compile(r'[^a-zA-Z0-9_]')  #脚本名只能是数字字母下划线
        rule = re.compile('^[a-zA-Z]{1}')  #脚本名只能以字母开头

        result = pattern.findall(data['name'])
        if len(result) != 0:
            print('[ERROR]支持使用字母、数字、下划线来为文件命名，必须以字母开头')
            return {'ok':False,'msg':'支持使用字母、数字、下划线来为文件命名，必须以字母开头'}
        else:
            if rule.match(data['name']) is None:
                print('[ERROR]支持使用字母、数字、下划线来为文件命名，必须以字母开头')
                return {'ok':False,'msg':'支持使用字母、数字、下划线来为文件命名，必须以字母开头'}
                
        path = os.path.join(workSpacePath, 'pages', data['name'] + '.py')
          
        if os.path.isfile(path):
            print(f'[ERROR]' + "脚本" + data['name'] + ".py" + "已存在")
            return {'ok':False,'exist':True,'msg':'文件名已存在'}
        file = open(path, 'w')
        file.close()

        casesList = []
        with open(os.path.join(workSpacePath, 'setting.UAUTO'), 'r', encoding='utf-8') as f:
            setting = json.load(f)
            for case in setting:
                casesList.append(case)
        newData = {
            "test_name": data['name'],
            "tag": data['caseName'],
            "run_case": data['name'],
        }
        casesList.append(newData)
        with open(os.path.join(workSpacePath, 'setting.UAUTO'), 'w', encoding='utf-8') as f:
            json.dump(casesList, f, ensure_ascii=False)
        print("脚本" + data['name'] + ".py"+ "创建成功")
        return {"ok": True, "msg": data['name']}
    except Exception as e:
        err_string = str(e).replace('\n','')
        print(f'[ERROR]{err_string}')
        logging.error(e)
        return {"ok": False, "msg": e}

# 添加脚本
def addFile():
    # window = tk.Tk()
    # window.withdraw()
    casesList = []
    # FilePath = filedialog.askopenfilenames(title = "请选择需要添加进工作区的脚本",initialdir=workSpacePath,filetypes=[('py','py')])
    
    result = []
    window = g_webview
    file_types = ('py (*.py)', 'All files (*.*)')        
    FilePath = window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=True, file_types=file_types)

    if FilePath:
        with open(os.path.join(workSpacePath, 'setting.UAUTO'), 'r', encoding='utf-8') as f:
            setting = json.load(f)
            for case in setting:
                casesList.append(case)

        for item in FilePath:
            file_name = item.split('\\')[-1].split('.')[0]
            with open(item, 'r', encoding='utf-8') as f:
                content = f.read()
                with open(os.path.join(workSpacePath, 'pages',file_name+".py"), "w" , encoding='utf-8') as file:
                    file.write(content)
                print("脚本" + file_name + ".py" + "已添加进工作区" + workSpacePath)    
            newData = {
                "test_name": file_name,
                "tag": file_name,
                "run_case": file_name
            }
            casesList.append(newData)

        with open(os.path.join(workSpacePath, 'setting.UAUTO'), 'w', encoding='utf-8') as f:
            json.dump(casesList, f, ensure_ascii=False)
        print("脚本添加成功")
        return {"ok": True, "msg": '添加脚本成功'}

    else:
        # window.destroy()
        print("已取消添加脚本")
        return ""

# 扫描指定文件夹下特定后缀的文件
def scan_files(directory, prefix=None, postfix=None):
    files_list = []

    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root, special_file))
            else:
                files_list.append(os.path.join(root, special_file))

    return files_list

def showItem():
    global phone
    if phone.isConnected:
        data = phone.showItem()
        data = json.loads(data)
        print(data)
        return {"ok": True, "msg": data}
        # return data

# 获取对应ID的GameObject详情
def get_inspector(data):
    global phone
    if phone.isConnected:
        d = phone.get_inspector(data['ID'])
        return {"ok": True, "msg": d}

# 暂停运行案例
def pause():
    global phone
    if phone.isConnected:
        phone.pause()
        return {"ok": True, "msg": '已停止'}


def continuePlay():
    global phone
    if phone.isConnected:
        phone.continuePlay()
        return {"ok": True, "msg": '已继续运行'}


def updateScripts(data):
    case = data['caseName'] or 'temp_test'
    if case == '':
        case = 'temp_test'
    data['caseName'] = case
    return loadCase(data)


def getTempFile():
    try:
        with open(os.path.join(workSpacePath, 'pages', 'temp_test.py'), 'r', encoding='utf-8') as f:
            return {"ok": True, "msg": f.read()}
    except Exception as e:
        err_string = str(e).replace('\n','')
        print(f'[ERROR]{err_string}')
        logging.error(e)
        return {"ok": False, "msg": e}


def connect(data):
    global phone
    try:
        res = phone.connect(data['sn'], data['ip'])
        return {"ok": True, "msg": res}
    except IndexError as ie:
        print(f'[ERROR]未找到设备号或IP')
        return {"ok": False, "msg": f"连接失败：请确认是否输入正确的设备号与IP"}
    except Exception as e:
        logging.error(e)
        err_string = str(e).replace('\n','')
        print(f'[ERROR]{err_string}')
        return {"ok": False, "msg": f"连接失败：{e}"}


def disConnect():
    # pass
    global phone
    # if phone.isConnected:
    phone.disConnect()
    return {"ok": True, "msg": f"已断开"}

def record(data):
    # pass
    global phone
    if phone.isConnected:
        case = data['caseName'] or 'temp_test'
        if case == '':
            case = 'temp_test'
        phone.record(CasePath(case + '.py'))
        return {"ok": True, "msg": '开始录制'}

def get_ip_address(serial):
    try:
        ip_str_arr = adb_helper.shell(serial, "ip route show").split("\n")
        for item1 in ip_str_arr:
            if "wlan" in item1 and "src" in item1:
                for index, item2 in enumerate(item1.split()):
                    if item2 == "src":
                        return item1.split()[index + 1]
    except:
        traceback.print_exc()
    return '0.0.0.0'


def get_connected_devices():
    print('-------------------------------------------')
    devices = helper.android_device_manager.get_connected_devices()
    logging.info(devices)
    dat = []
    for e in devices:
        # ip = '127.0.0.1'
        ip = get_ip_address(e.serial)
        dat.append({'name': e.device_name, 'sn': e.serial, 'ip': ip})
        logging.info(f'{e}, {ip}')
    return {"ok": True, "msg": dat}


# 当前连接状态
def checkConnection():
    return {"ok": True, "msg": phone.checkConnection()}


# 保存temp脚本
def saveTempFile(s):
    with open(os.path.join(workSpacePath, 'pages', 'temp_test.py'), 'w', encoding='utf-8') as f:
        f.write(s)
    return {"ok": True, "msg": "保存成功"}


# 保存脚本
def saveFile(name, s):
    global workSpacePath
    with open(os.path.join(workSpacePath, 'pages', name + '.py'), 'w') as f:
        f.write(s)
    return {"ok": True, "msg": "保存成功"}

def get_u3driver_version():
    global phone
    status = None
    if phone != None:
        status = phone.get_version()
    return {"ok": status != None, "msg": status}

# 打开Demo
def openDemo():
    global phone
    while len(phone.GetDevices()) != 1:
        time.sleep(1)
    while not phone.isInstalled():
        phone.installDemo()
        time.sleep(2)
    phone.openAPP()
    return {"ok": True, "msg": "已打开Demo"}


def getDemoScripts():
    with open(os.path.join(ROOT_DIR, 'asset', 'demo.py'), 'r') as f:
        res = f.read()
        return {"ok": True, "msg": res}


def LoadModuleByPath(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def CasePath(name):
    return os.path.join(workSpacePath, 'pages', name)
    # return os.path.join(ROOT_DIR, 'asset', name)


def runCase(data):
    global phone
    if phone.isConnected:
        # case = importlib.import_module('miniperf.asset.temp_test')
        # temp_test = importlib.util.find_loader('temp_test', os.path.join(ROOT_DIR, 'asset', 'temp_test.py'))
        try:
            case = data['caseName'] or 'temp_test'
            if case == '':
                case = 'temp_test'
            saveTempFile(data['fileInfo'])
            saveFile(data['caseName'], data['fileInfo'])
            module = LoadModuleByPath(case, CasePath(case + ".py"))
            module.AutoRun(phone.device)
            print("运行完成")
            return {"ok": True, "msg": '运行完成'}
        except Exception as e:
            err_string = str(e).replace('\n','')
            print(f'[ERROR]{err_string}')
            logging.error(e)
            print("[ERROR]运行失败")
            return {"ok": False, "msg": f'运行失败:{e}'}


# 是否为新用户
def isNewUser():
    return {"ok": True, "msg": config.getboolean('General', 'new_user')}


# 通过VS CODE打开工作区
def openInVS():
    try:
        os.popen(f'code {workSpacePath}')
        return {"ok": True, "msg": '已打开'}
    except:
        return {"ok": False, "msg": '出错'}


# 修改Config
def setConfig(section, name, value):
    config.set(section, name, value)
    config.write(open(configPath, "w", encoding='UTF-8'))


# 完成新用户设置
def finishNewUser():
    config.set('General', 'new_user', 'False')
    config.write(open(configPath, "w", encoding='UTF-8'))
    return {"ok": True, "msg": '设置完成'}


# 安装Demo
def installDemo():
    global phone
    msg = phone.installDemo()
    return {"ok": True, "msg": msg}


# 是否安装了指定包名的应用
def isInstalled():
    global phone


# 暂停录制
def recordPause():
    global phone
    phone.recordPause()
    print('已暂停录制')
    return {"ok": True, "msg": '已暂停录制'}

# 停止录制
def recordStop():
    global phone
    phone.recordStop()
    print('已停止录制')
    return {"ok": True, "msg": '已停止录制'}

# 继续录制
def recordResume():
    global phone
    phone.recordResume()
    print('继续录制')
    return {"ok": True, "msg": '继续录制'}

def is_debug_mode_record():
    global phone
    return {"ok": phone.is_debug_mode_record(), "msg": ''}

# def registered_webview(webview):
#     global g_webview
#     g_webview = webview


# def mkdir_if_not_exists(path, *paths):
#     dirname = os.path.join(path, *paths)
#     if not os.path.exists(dirname):
#         os.mkdir(dirname)
#     return dirname


# def external_data_dir():
#     return mkdir_if_not_exists(ROOT_DIR, ".data")


# def post_message_to_js(msg, type):
#     global g_webview
#     if g_webview:
#         g_webview.send_message_to_js(
#             {"type": "on_message", "data": {"type": type, "msg": msg}})


# def select_app(window):
#     files = window.show_file_dialog_for_file("选择要监控的应用", "应用程序(*.exe)")
#     if files and len(files) > 0:
#         try:
#             file = files[0]
#             logging.info("import file %s", file)
#             return {"ok": True, "msg": file}
#         except Exception as err:
#             print('Exception', err)
#             traceback.print_exc()
#             return {"ok": False, "msg": "无法选择应用"}
#     return {"ok": False, "msg": "未选择文件"}


# def get_scrcpy():
#     global phone
#     if phone == None:
#         return
#     res = phone.screenshot()
#     print('img:', res)
#     return res.convert("RGB")


# def loadTree():
#     with open(r"D:\frontProject\pywebview\miniperf\asset\data.json", 'r') as f:
#         loadData = json.load(f)
#         print(loadData)
#         return {"ok": True, "msg": loadData}


# def get_cstemplate_file():
#     return os.path.join(ROOT_DIR, "asset", "template", "CSTemplate.cs")


# def get_tpsvn():
#     return os.path.join(ROOT_DIR, "asset", "tpsvn", "svn.exe")


# def rpc_open_folder(dir):
#     if '.cs' in dir:
#         dir = os.path.dirname(dir)
#     open_dir(dir)
#     return {"ok": True, "dat": f"{dir}"}


# def rpc_get_default_setting(app):
#     xlsx_path = app.get_config("Settting/XLSX_PATH", os.path.join(".", "configs.ini"))
#     cscode_path = app.get_config("Settting/CSCODE_PATH", os.path.join(".", "configs.ini"))
#     csmgr_path = app.get_config("Settting/MGR_PATH", os.path.join(".", "configs.ini"))
#     tab_path = app.get_config("Settting/TAB_PATH", os.path.join(".", "configs.ini"))
#     dat = {
#         "XLSX_PATH": xlsx_path,
#         "CSCODE_PATH": cscode_path,
#         "TAB_PATH": tab_path,
#         "MGR_PATH": csmgr_path
#     }
#     return {"ok": True, "dat": dat}


# def return_log():
#     pass


# def readOut(process):
#     logging.info("readOut")
#     for readOut_line in process.stdout:
#         if len(readOut_line) < 1:
#             break
#         readOut_line = readOut_line.decode("utf-8")
#         logging.info("readOut: %s", readOut_line)
#         post_message_to_js(readOut_line, "out")


# def readErr(process):
#     logging.info("readErr")
#     for readErr_line in process.stderr:
#         if len(readErr_line) < 1:
#             break
#         readErr_line = readErr_line.decode("utf-8")
#         logging.info("readErr: %s", readErr_line)
#         post_message_to_js(readErr_line, "out")


# def open_dir(report_dir):
#     logging.info("open_dir")
#     os.startfile(report_dir)
