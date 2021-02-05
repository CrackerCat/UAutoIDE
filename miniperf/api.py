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
        return extension.connect(data['sn'])
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

    def get_file_list(xlsxpath):
        file_list = []
        try:
            files_status = extension.get_svn_status(xlsxpath)
            print(files_status)

            files = glob.glob(xlsxpath + '/**/*.xls*', recursive=True)
            for f in files:
                if not os.path.basename(f).startswith('~'):
                    status = files_status.get(f, 'o')
                    file_list.append({'name': os.path.basename(f), 'path': f, 'status': status})

            
            # list = output.replace(' ', '')
            # list = list[2:]
            # list = list.split(r'\n')        
            # for f in list:
            #     name = f[1:-2].split(r'\\')[-1]
            #     if 'xls' in name and not name.startswith('~'):
            #         file_list.append({'name': name, 'path': f[1:-2].replace('\\\\','\\'), 'status':f[0]})
        except Exception as e:
            print(e)
            files = glob.glob(xlsxpath + '/**/*.xls*', recursive=True)
            for f in files:
                if not os.path.basename(f).startswith('~'):
                    file_list.append({'name': os.path.basename(f), 'path': f, 'status':'o'})
        # print(xlsxpath)
        # files = glob.glob(xlsxpath + '/**/*.xls*', recursive=True)
        # for f in files:
        #     if not os.path.basename(f).startswith('~'):
        #             file_list.append({'name': os.path.basename(f), 'path': f})
        print(file_list)
        return file_list