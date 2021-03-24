import logging
import os
import sys
import time
import datetime
import json
import re
import webview

from miniperf import extension
from miniperf import api
from miniperf import helper
from miniperf.device_manager import DeviceManager


class ColorHandler(logging.StreamHandler):
    _colors = dict(black=30, red=31, green=32, yellow=33,
                   blue=34, magenta=35, cyan=36, white=37)

    def emit(self, record):
        msg_colors = {
            logging.DEBUG: "\x1b[0m",
            logging.INFO: "\x1b[0m",
            logging.WARNING: "\x1b[%s;0m" % self._colors["yellow"],
            logging.ERROR: "\x1b[%s;0m" % self._colors["red"]
        }

        color = msg_colors.get(record.levelno, "\x1b[0m")
        self.stream.write(color)
        super().emit(record)
        self.stream.write("\x1b[0m")


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

console = ColorHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(fmt='%(asctime)s %(thread)d %(threadName)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
logging.getLogger('').setLevel(logging.DEBUG)


logger = logging.getLogger(os.path.basename(__file__))

g_serials = {}
def _get_device_name(serial):
    if serial in g_serials:
        return g_serials[serial].device_name
    return None

def get_android_device_name(serial):
    devices = helper.android_device_manager.get_connected_devices()
    for device in devices:
        if device.serial == serial:
            return device.device_name
    return None

def get_android_device_ip(serial):
    # ip = ghelper.android_device_manager.get_device_ip(serial)
    ip = '127.0.0.1'
    logging.info(f'ip={ip}')

class DeviceChangeListener(object):

    def __init__(self,window):
        self.window = window

    def on_device_connect(self, device):
        device_name = get_android_device_name(device.serial)
        is_android = True
        self.notify_webview_device_changed(device.serial, device_name, True)
        logging.info("on_device_connect serial=%s device_name=%s os=%s" % (device.serial, device_name, "Android" if is_android else "iOS"))
        logging.info(get_android_device_ip(device.serial))

    def on_device_disconnect(self, device):
        device_name = _get_device_name(device.serial)
        self.notify_webview_device_changed(device.serial, device_name, False)
        logging.info("on_device_disconnect %s %s" % (device.serial, device.device_name))

    def notify_webview_device_changed(self, serial, device_name, is_connected):
        logging.info(f'notify_webview_device_changed  {serial}, {device_name}, {is_connected}')
        extension.isNotChanged = False
        # global g_webview
        # if g_webview:
        #     g_webview.send_message_to_js({"type": "on_device_changed", "data": {"serial": serial, "deviceName": device_name, "isConnected": is_connected}})




def api_ls():
    if len(webview.windows) > 0:
        webview.windows[0].evaluate_js('window.pywebview.api.ls()')
    else:
        print('---api_ls---')


def on_closed():
    print('pywebview window is closed')


def on_closing():
    extension.disConnect()
    print('pywebview window is closing')


def on_shown():
    print('pywebview window shown')


def on_loaded():
    print('DOM is ready')
    # unsubscribe event listener
    webview.windows[0].loaded -= on_loaded
    # webview.windows[0].evaluate_js('window.pywebview.api.ls()')
    # webview.windows[0].load_url('https://google.com')


def main():
    data_dir = os.path.abspath(os.path.join(".", "data"))
    log_dir = os.path.join(data_dir, "log")
    report_dir = os.path.join(data_dir, "report")
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(log_dir, exist_ok=True)
    os.makedirs(report_dir, exist_ok=True)

    static_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ui", "index.html")
    # print(static_file)
    # window  = webview.create_window('TableConvertTool', html=html, background_color='#333333', js_api=api.Api())
    window = webview.create_window('UAutoIDE', os.path.join(os.path.dirname(os.path.abspath(__file__)), "ui", "index.html"), width=1366, height=800, js_api=api.Api())
    window.closed += on_closed
    window.closing += on_closing
    window.shown += on_shown
    window.loaded += on_loaded

    device_change_listener = DeviceChangeListener(window)
    helper.android_device_manager = DeviceManager()
    helper.android_device_manager.register_device_change_listener(device_change_listener)

    # webview.start(api_ls, gui='cef', http_server=True, debug=True)
    if sys.platform == 'darwin':
        webview.start(func=api_ls, debug=True)
    else:
        webview.start(gui='cef', func=api_ls, debug=True)


if __name__ == "__main__":
    main()
