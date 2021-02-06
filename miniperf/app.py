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
formatter = logging.Formatter(fmt='%(asctime)s %(thread)d %(threadName)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                              datefmt='%a, %d %b %Y %H:%M:%S')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
logging.getLogger('').setLevel(logging.DEBUG)

def api_ls():
    if len(webview.windows) > 0:
        webview.windows[0].evaluate_js('window.pywebview.api.ls()')
    else:
        print('---api_ls---')

def on_closed():
    print('pywebview window is closed')


def on_closing():
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
    window  = webview.create_window('TableConvertTool', os.path.join(os.path.dirname(os.path.abspath(__file__)), "ui", "index.html"), js_api=api.Api())
    window.closed += on_closed
    window.closing += on_closing
    window.shown += on_shown
    window.loaded += on_loaded

    # webview.start(api_ls, gui='cef', http_server=True, debug=True)
    webview.start(gui='cef', func=api_ls, debug=True)

if __name__ == "__main__":
    main()
