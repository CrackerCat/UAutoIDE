import json
import os
import subprocess

from u3driver import AltrunUnityDriver, By

demoPackageName = 'com.DefaultName.DefaultName'
demoPackageActivity = 'com.unity3d.player.UnityPlayerActivity'

class Device:
    def __init__(self, ROOT_DIR, serial_num=''):
        self.serial_num = serial_num
        self.screenshot_path = os.path.join('C:\image', 'screenshot_pic')
        self.tempFilePath = os.path.join(ROOT_DIR, 'asset', 'temp_test.py')
        self.adbPath = os.path.join(ROOT_DIR,'asset','ADB','adb.exe')
        self.demoPath = os.path.join(ROOT_DIR, 'asset', 'demo.apk')
        # if not serial_num == '':
        #     ip = self.getIP()
        #     self.device = AltrunUnityDriver(serial_num, '', ip)
        #     self.__isConnected = True
        # else:
        #     self.__isConnected = False
        if not serial_num == '':
            ip = self.getIP()
            self.device = AltrunUnityDriver(serial_num, '', ip)
        pass

    @property
    def isConnected(self):
        try:
            return self.device.connect and getattr(self.device.socket, '_closed') is False
        except:
            return False

    def connect(self, serial_num, ip):
        self.serial_num = serial_num
        if ip == '':
            ip = self.getIP()
        self.device = AltrunUnityDriver(serial_num, '', ip)
        # self.isConnected = True
        return ip

    def disConnect(self):
        self.device.stop()
        # self.isConnected = False

    def test(self):
        return self.tempFilePath

    def showItem(self):
        return self.device.get_hierarchy()

    def checkConnection(self):
        status = {}
        status['isConnected'] = self.isConnected
        return status

    # 暂停运行案例
    def pause(self):
        self.device.Pause(True)

    # 继续运行案例
    def continuePlay(self):
        self.device.Pause(False)

    # 是否安装了指定包名的应用
    def isInstalled(self):
        res = os.popen(f"{self.adbPath} shell pm path {demoPackageName}").read()
        if res is not '':
            return True
        else:
            return False

    # 打开应用
    def openAPP(self,packageName = demoPackageName,activity = demoPackageActivity):
        res = os.popen(f"{self.adbPath} shell am start -n {packageName}/{activity} ").read()
        return res

    # 获取对应ID的GameObject详情
    def get_inspector(self,id):
        s = self.device.get_inspector(id)
        data = json.loads(s)
        return data
    # def screenshot(self):
    #     adb = adb_path()
    #     cmdline = adb + ' -s ' + self.serial_num + ' shell screencap -p'
    #     # windows
    #     # return subprocess.Popen(cmdline, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read()
    #     # linux
    #     return subprocess.Popen(cmdline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read()

    def record(self):
        self.device.debug_mode(self.tempFilePath)

    # 安装Demo
    def installDemo(self):
        res = os.popen(f"{self.adbPath} install -g {self.demoPath}").read()
        return res

    def getIP(self):
        try:
            res = os.popen(f"{self.adbPath} -s {self.serial_num} shell ifconfig").read()
            ip = res.split('wlan0')[1].split('inet addr:')[1].split(' ')[0]
            return ip
        except:
            res = os.popen(f'{self.adbPath} -s {self.serial_num} shell netcfg').read()
            ip = res.split('wlan0')[1].split('UP')[1].split('/')[0].split()[0]
            return ip

    def getTempFile(self):
        with open(self.tempFilePath, 'r') as f:
            return f.read()

    def saveTempFile(self,s):
        with open(self.tempFilePath, 'w',encoding='utf-8') as f:
            return f.write(s)

    def screenshot(self, filename=None, format='pillow'):
        """ screenshot, Image format is JPEG
        Args:
            filename (str): saved filename
            format (str): used when filename is empty. one of "pillow" or "opencv"
        Examples:
            screenshot("saved.jpg")
            screenshot().save("saved.png")
            cv2.imwrite('saved.jpg', screenshot(format='opencv'))
        Return:
            screenshot result
        """
        try:
            # self.logger.info('--screenshot-- filename=' + filename)
            return self.device.screenshot(filename, format)
        except Exception as e:
            # self.logger.error('--screenshot-- failed!!!!! Exception=' + str(e), exc_info=True)
            return None
