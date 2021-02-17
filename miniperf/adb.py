import json
import os
import subprocess

from u3driver import AltrunUnityDriver, By

class Device:
    def __init__(self,tempFilePath,serial_num = ''):
        self.serial_num = serial_num
        self.screenshot_path = os.path.join('C:\image', 'screenshot_pic')
        self.tempFilePath = os.path.join(tempFilePath,'asset','temp_test.py')
        if not serial_num == '':
            ip = self.getIP()
            self.device = AltrunUnityDriver(serial_num, '', ip)
            self.isConnected = True
        else:
            self.isConnected = False
        pass

    def connect(self,serial_num,ip):
        self.serial_num = serial_num
        if ip == '':
            ip = self.getIP()
        self.device = AltrunUnityDriver(serial_num,'',ip)
        self.isConnected = True
        return ip

    def disConnect(self):
        self.device.stop()
        self.isConnected = False

    def test(self):
        return self.tempFilePath

    def showItem(self):
        return self.device.get_all_object()
    # def screenshot(self):
    #     adb = adb_path()
    #     cmdline = adb + ' -s ' + self.serial_num + ' shell screencap -p'
    #     # windows
    #     # return subprocess.Popen(cmdline, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read()
    #     # linux
    #     return subprocess.Popen(cmdline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read()

    def record(self):
        self.device.debug_mode(self.tempFilePath)

    def getIP(self):
        try:
            res = os.popen(f"adb -s {self.serial_num} shell ifconfig").read()
            ip = res.split('wlan0')[1].split('inet addr:')[1].split(' ')[0]
            return ip
        except:
            res = os.popen(f'adb -s {self.serial_num} shell netcfg').read()
            ip = res.split('wlan0')[1].split('UP')[1].split('/')[0].split()[0]
            return ip

    def getTempFile(self):
        with open(self.tempFilePath, 'r') as f:
            return f.read()

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
