import json
import os

from u3driver import AltrunUnityDriver, By
from miniperf import device_manager
from miniperf import extension
import threading
import ctypes
import inspect
demoPackageName = 'com.DefaultName.DefaultName'
demoPackageActivity = 'com.unity3d.player.UnityPlayerActivity'
is_get_version = True
status = {}

def _async_raise(tid, exctype):
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
    
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

class DeviceThread(threading.Thread):
    def __init__(self, target_func,serial_num,ip,  *args, **kwargs):
        super(DeviceThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()
        self.target_func = target_func
        self.finishConnected = False
        self.serial_num = serial_num
        self.ip = ip
        data = self.target_func(self.serial_num,self.ip)

    def run(self):
        pass

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def _get_my_tid(self):
    
        if not self.isAlive():
            raise threading.ThreadError("the thread is not active")

        if hasattr(self, "_thread_id"):
            return self._thread_id

        for tid, tobj in threading._active.items():
            if tobj is self:
                self._thread_id = tid
                return tid

        raise AssertionError("could not determine the thread's id")

    def raiseExc(self, exctype):
        _async_raise(self._get_my_tid(), exctype )

class Device:
    def __init__(self, ROOT_DIR,serial_num=''):
        self.serial_num = serial_num
        self.screenshot_path = os.path.join('C:\image', 'screenshot_pic')
        self.tempFilePath = os.path.join(ROOT_DIR, 'asset', 'temp_test.py')
        self.adbPath = os.path.join(ROOT_DIR,'asset','ADB','adb.exe')
        self.demoPath = os.path.join(ROOT_DIR, 'asset', 'demo.apk')
        # devices = DeviceThread()
        # self.finishConnected = DeviceThread.finishConnected
        self.finishConnected = False
        pass
    
    def connectcheck(self,serial_num, ip):
        try:
            self.device = AltrunUnityDriver(serial_num, '', ip)
            self.finishConnected = True    
        except self.thread.ThreadStopped:
            pass

    @property
    def isConnected(self):
        try:
            return self.finishConnected
        except:
            return False

    def connect(self, serial_num, ip):
        self.serial_num = serial_num
        if ip == '':
            ip = extension.get_ip_address(serial_num)
        # self.device = AltrunUnityDriver(serial_num, '', ip)
        # self.isConnected = True
        # self.connectcheck(serial_num,ip)
        self.thread = DeviceThread(target_func=self.connectcheck,serial_num = serial_num,ip = ip)
        # self.finishConnected = self.thread.finishConnected
        self.thread.start()

        return

    def disConnect(self):
        self.device.stop()
        self.thread.stop()
        # stop_thread(self.thread)
        self.finishConnected = False


    def test(self):
        return self.tempFilePath

    def showItem(self):
        return self.device.get_hierarchy()

    def get_version(self):
        status = {}
        if self.device != None and self.isConnected:
            status['ip'] = extension.get_ip_address(self.device.appium_driver)
            status['version'] = self.device.get_server_version()
        return status

    def checkConnection(self):
        status = {}
        status['isConnected'] = self.isConnected
        return status

    # 暂停运行案例
    def pause(self):
        self.device.Pause(True)

    # 暂停录制
    def recordPause(self):
        self.device.debug_mode_pause()

    # 停止录制
    def recordStop(self):
        self.device.debug_mode_stop()

    # 继续录制
    def recordResume(self):
        self.device.debug_mode_resume()

    # 继续运行案例
    def continuePlay(self):
        self.device.Pause(False)

    def is_debug_mode_record(self): 
        return self.device.is_debug_mode_record()

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

    def record(self,path):
        self.device.debug_mode(path)

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

    def GetDevices(self):
        devices = os.popen(f"{self.adbPath} devices").read()
        devices = devices.split('\n')
        devicesList = []
        for i in range(1, len(devices)):
            if devices[i] != '':
                devices_dir = {}
                device_number = devices[i].replace('device', "").split('\t')[0]
                device_name = os.popen(f'{self.adbPath} -s ' + device_number + ' shell getprop ro.product.model ').read()
                device_name = device_name.replace("\n", "")
                devices_dir['name'] = device_name
                devices_dir['sn'] = device_number
                devicesList.append(devices_dir)
        return devicesList