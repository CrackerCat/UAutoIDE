# coding: utf-8
import os, re
from setuptools import setup, find_namespace_packages

with open(os.path.join("miniperf", "__init__.py"), encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name='miniperf',
    version=version,
    python_requires='>=3.6',
    description='miniperf',
    url='https://github.com/king3soft/UAutoIDE',
    author='king3soft',
    author_email='buutuud@gmail.com',
    license='GPLv3',
    include_package_data=True,
    packages=find_namespace_packages(include=['miniperf.*', "miniperf"]),
    install_requires='''u3driver
    '''.split('\n'),
    zip_safe=False)