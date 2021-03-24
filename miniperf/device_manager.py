import logging
import traceback

from miniperf import adb_helper
from miniperf.singleton import Singleton


class Device(object):

    def __init__(self, serial, device_name, model=None):
        self.serial = serial
        self.device_name = device_name
        self.model = model

    def is_connected(self):
        """Check if this device has been connected"""
        return False

    def __eq__(self, other):
        return self is not None and other is not None and self.serial == other.serial
        # and self.device_name == other.device_name

    def __str__(self):
        return "[Device, serial=%s, device_name=%s]" % (str(self.serial), str(self.device_name))


class DeviceManager(object, metaclass=Singleton):
    """Device Manager"""

    last_device = None
    current_device = None
    device_change_listeners = []
    installed_apps = None

    def __init__(self):
        self.init()

    def init(self):
        adb_helper.init()
        self.track_devices()

    def get_connected_devices(self):
        """Get all connected devices list"""
        return list(map(lambda d: Device(d.serial, d.device_name, d.model), adb_helper.devices()))

    def get_installed_apps(self, use_cache=False):
        """Get all installed applications of current device"""
        if self.current_device is None:
            return []
        if self.installed_apps is None or not use_cache:
            self.installed_apps = adb_helper.get_packages(self.current_device.serial) #list(map(lambda p: App(p), adb_helper.get_packages(self.current_device.serial)))
        return self.installed_apps

    def has_connected_device(self):
        return True

    def register_device_change_listener(self, listener):
        self.device_change_listeners.append(listener)

    def unregister_device_change_listener(self, listener):
        if listener in self.device_change_listeners:
            self.device_change_listeners.remove(listener)

    def notify_device_change_listeners(self, event):
        if event.what is adb_helper.TrackEvent.DEVICE_EVENT_CONNECT:
            for listener in self.device_change_listeners:
                listener.on_device_connect(Device(event.device, None))
        elif event.what is adb_helper.TrackEvent.DEVICE_EVENT_DISCONNECT:
            self.current_device = None
            for listener in self.device_change_listeners:
                listener.on_device_disconnect(Device(event.device, None))
        elif event.what is adb_helper.TrackEvent.TRACKER_DIED:
            logging.error("Tracker Died")
            self.current_device = None
            for listener in self.device_change_listeners:
                listener.on_device_disconnect(Device(event.device, None))
            self.track_devices()

    def track_devices(self):
        try:
            adb_helper.track_devices(self.notify_device_change_listeners)
        except:
            logging.exception("track devices fail")

    def set_current_device(self, device):
        if self.current_device is not device:
            self.current_device = device
            self.last_device = device

    def get_current_device(self):
        if self.current_device is not None:
            return self.current_device
        else:
            devices = self.get_connected_devices()
            if len(devices) > 0:
                self.set_current_device(devices[0])
                return devices[0]
        return None

    def get_last_device(self):
        return self.last_device

    def shell(self, cmd):
        if self.current_device is None:
            raise Exception('Current Device is None')
        logging.info("Send Shell Cmd %s" % cmd)
