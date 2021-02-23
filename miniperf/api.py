import glob
import json
import subprocess
import webview
import os
from miniperf import extension
import sys
import subprocess
class Api:

    def __init__(self):
        self.output = []
        self.stdoutbak = sys.stdout
        self.stderrbak = sys.stderr
        sys.stdout = self
        sys.stder = self
        extension.initWorkSpace()
        # self.p = subprocess.Popen('python miniperf/Test.py',stdin=subprocess.PIPE)

    def connect(self, data):
        # print(data)
        # self.p.stdin.write("data")
        # self.p.stdin.flush()
        return extension.connect(data)
    def disConnect(self):
        return extension.disConnect()

    def checkConnection(self):
        return extension.checkConnection()

    def write(self, info):
        self.output.append(info)

    def restoreStd(self):
        sys.stdout = self.stdoutbak
        sys.stderr = self.stderrbak

    def pywebviewready(self):
        print('pywebviewready')
    
    def on_HomeClick(self):
        print('on_HomeClick')
        
    def fullscreen(self):
        webview.windows[0].toggle_fullscreen()

    def save_content(self, content):
        filename = webview.windows[0].create_file_dialog(webview.SAVE_DIALOG)
        print(filename)
        if not filename:
            return

        with open(filename, 'w') as f:
            f.write(content)

    def ls(self):
        print('ls')
        return os.listdir('.')


    def record(self):
        return extension.record()

    def test(self):
        return extension.createWorkSpace(r'D:\RunCaseTest','jsxxxx')

    # 暂停案例运行
    def pause(self):
        return extension.pause()

    # 继续脚本运行
    def continuePlay(self):
        return extension.continuePlay()

    # 保存temp案例
    def saveTempFile(self,data):
        return extension.saveTempFile(data['fileInfo'])

    def updateScripts(self):
        return extension.getTempFile()

    def showItem(self):
        return extension.showItem()

    def PythonOutput(self):
        if len(self.output) > 0:
            # temp = self.output.pop(0)
            temp = ''
            for s in self.output:
                temp += s
            self.output.clear()
            return temp
        return '405null'

    def runCase(self,data):
        return extension.runCase(data)
    def getCurDevice(self):
        return extension.getCurDevice()

    # 获取对应ID的GameObject详情
    def get_inspector(self,data):
        return extension.get_inspector(data)

    # 安装Demo
    def installDemo(self):
        return extension.installDemo()

    # # 是否安装了指定包名的应用
    # def isInstalled(self,name):

    def openDemo(self):
        return extension.openDemo()

    def getDemoScripts(self):
        return extension.getDemoScripts()

    # 是否为新用户
    def isNewUser(self):
        return extension.isNewUser()

    # 完成新用户设置
    def finishNewUser(self):
        return extension.finishNewUser()

    # 加载指定名称的脚本
    def loadCase(self,data):
        return extension.loadCase(data)

    # 加载本地脚本列表
    def loadCasesList(self):
        return extension.loadCasesList()
