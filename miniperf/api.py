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
        # self.p = subprocess.Popen('python miniperf/Test.py',stdin=subprocess.PIPE)

    def connect(self, data):
        # print(data)
        # self.p.stdin.write("data")
        # self.p.stdin.flush()
        return extension.connect(data)
    def disConnect(self):
        return extension.disConnect()


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
        return extension.getTempFile()

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

    def runCase(self):
        return extension.runCase()

    def getCurDevice(self):
        return extension.getCurDevice()
