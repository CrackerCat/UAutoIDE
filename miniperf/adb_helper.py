import sys
import os
import socket
import struct
import subprocess
from functools import wraps
from adb import AdbConnectionError, UnexpectedDataError
from adb.client import Client as AdbClient
from adb.protocol import Protocol
from adb.sync import Sync
import logging
import random
import re
import posixpath
from threading import Lock
import shutil
import time

_dirname_ = os.path.abspath(os.path.dirname(__file__))
logger = logging.getLogger(os.path.basename(__file__))

gAdbNonce = None
gAdbRestartLock = Lock()
ADB_PORT = 5037
gAdbClient = None

def init():
    global gAdbClient
    gAdbClient = AdbClient(port=ADB_PORT)

class TrackEvent:
    DEVICE_EVENT_CONNECT = 1
    DEVICE_EVENT_DISCONNECT = 2
    TRACKER_DIED = 3

    def __init__(self, what, device):
        self.what = what
        self.device = device

def find_adb_path():
    #return r'd:\tools\android\sdk\platform-tools\adb.exe'
    #return r'C:\Users\Admin\AppData\Local\Android\sdk\platform-tools\adb.exe'
    #ret = shutil.which("adb")
    #if ret:
    #    return ret
    return os.path.join(_dirname_, 'asset', 'adb', 'adb.exe')


ADB_PATH = find_adb_path()


def restart_adb():
    global gAdbNonce
    before = gAdbNonce
    with gAdbRestartLock:
        if gAdbNonce != before: return
        logging.warning("restarting adb")
        subprocess.check_call([ADB_PATH, '-P', str(ADB_PORT), 'start-server'])
        gAdbNonce = random.randint(1, 10000000)

if sys.platform == 'win32':
    def maybe_restart_adb(retries=3):
        def deco(fun):
            @wraps(fun)
            def _wrapper(*largs, **kwargs):
                _t = retries
                while _t > 0:
                    _t -= 1
                    try:
                        return fun(*largs, **kwargs)
                    except (AdbConnectionError, UnexpectedDataError, ConnectionResetError):
                        logging.exception(str(fun))
                        restart_adb()
                return fun(*largs, **kwargs)
            return _wrapper
        return deco
else:
    def maybe_restart_adb(retries=3):
        def deco(func):
            return func
        return deco

@maybe_restart_adb()
def _track_devices(callback):
    gAdbClient.track_devices(callback)


def track_devices(callback):
    def _callback(msg):
        logging.info("adb ----------- %s", msg)
        if msg.startswith("device online"):
            serial = msg.split(":", 1)[1].strip()
            callback(TrackEvent(TrackEvent.DEVICE_EVENT_CONNECT, serial))
        elif msg.startswith("device gone"):
            serial = msg.split(":", 1)[1].strip()
            callback(TrackEvent(TrackEvent.DEVICE_EVENT_DISCONNECT, serial))
        elif msg == "connection lost":
            callback(TrackEvent(TrackEvent.TRACKER_DIED, None))
            #restart_adb()
        else:
            logging.error("[track_device] unknown message: %r" % msg)
    _track_devices(_callback)

ptn_pkg_uid = re.compile(r'\s+Package\s+\[(?P<pkg>[^\]]+)\].*userId=(?P<uid>\d+)')

def _match_pkg_uid(line):
    mo = ptn_pkg_uid.match(line)
    if not mo:
        #print("--------- ", line)
        return None
    return (int(mo.groupdict()['uid']), mo.groupdict()['pkg'])

def get_uid_map(serial):
    text = gAdbClient.device(serial).shell("dumpsys package | grep -B1 userId")
    return dict(filter(None, map(_match_pkg_uid, map(lambda x: x.replace('\n',''), text.split('--')))))

def open_logcat(serial, callback, clear=False):
    uidmap = get_uid_map(serial)
    class LogcatWrapper:
        def __init__(self):
            self.more = True

        def cb(self, obj):
            try:
                if obj['what'] == 'log':
                    if 'uid' in obj['msg']:
                        obj['msg']['package'] = uidmap.get(int(obj['msg']['uid']), b'?')
                    else:
                        obj['msg']['package'] = b'?'
                callback(obj)
            except:
                logging.exception("error in logcat")
                pass
            return self.more

        def close(self):
            self.more = False

    logcat = LogcatWrapper()
    gAdbClient.device(serial).open_logcat(logcat.cb, clear=clear)
    return logcat

@maybe_restart_adb()
def devices():
    return gAdbClient.devices_with_path()


@maybe_restart_adb()
def get_all_packages(serial):
    return gAdbClient.device(serial).list_packages()

@maybe_restart_adb()
def get_packages(serial):
    """
    get all third party packages
    :param serial: serial of device
    :return: list of packages
    """
    result = gAdbClient.device(serial).shell("pm list packages -3 2>/dev/null")
    result_pattern = "^package:(.*?)\r?$"
    packages = []
    for line in result.split('\n'):
        m = re.match(result_pattern, line)
        if m:
            packages.append(m.group(1))
    return packages

def is_package_running(serial, package):
    return bool(get_pids(serial, package))

@maybe_restart_adb()
def stop_package(serial, package):
    gAdbClient.device(serial).shell("am force-stop %s >/dev/null 2>&1" % package)


@maybe_restart_adb()
def start_package(serial, package):
    gAdbClient.device(serial).shell("monkey -p %s -c android.intent.category.LAUNCHER 1 >/dev/null 2>&1" % package)


@maybe_restart_adb()
def push(serial, local, remote):
    gAdbClient.device(serial).push(local, remote)


@maybe_restart_adb()
def pull(serial, local, remote):
    gAdbClient.device(serial).pull(remote, local)

@maybe_restart_adb()
def shell(serial, cmd, timeout=None):
    return gAdbClient.device(serial).shell(cmd, timeout=timeout)

@maybe_restart_adb()
def get_native_libs(serial, package):
    out = gAdbClient.device(serial).shell("pm path %s" % package)
    matched = re.match(r'[^/]+(?P<path>.*)', out)
    if not matched: return None
    path = matched.groupdict()['path']
    libpath = posixpath.join(posixpath.dirname(path), "lib")
    out = gAdbClient.device(serial).shell("find %s" % libpath)
    so_list = list(filter(lambda s: s.endswith(".so"), map(lambda s: os.path.basename(s.strip()), out.split('\n'))))
    print("package", package, "so_list", so_list)
    return so_list
    #out = gAdbClient.device(serial).shell("find /data/app/%s*" % package)
    #return list(filter(lambda s: s.endswith(".so"), map(str.strip, out.split('\n'))))

@maybe_restart_adb()
def has_native_lib(serial, package, lib_so_file_name):
    so_list = get_native_libs(serial, package)
    return lib_so_file_name in so_list

@maybe_restart_adb()
def has_native_libs(serial, package, lib_so_file_name_list):
    so_list = get_native_libs(serial, package)
    if not so_list:
        return False
    for lib_so_file_name in lib_so_file_name_list:
        if lib_so_file_name not in so_list:
            return False
    return True

@maybe_restart_adb()
def is_zygote_injected(serial):
    pids= get_pids(serial, "zygote")
    if len(pids) != 1:
        logging.warning("too many or no zygote process: %r" % pids)
        return False
    out = gAdbClient.device(serial).shell("su -c cat /proc/%d/maps 2>/dev/null| grep libzyg" % pids[0]).strip()
    return True if out.strip() else False

@maybe_restart_adb()
def get_pids_slow(serial, name):
    """
    walk through the /proc dir, read every cmdline and compare that against the `name`, print if matched
    :param serial:
    :param name: process name
    :return: list of `pid`s that matched
    """
    out = gAdbClient.device(serial).shell("for i in `ls /proc`;do if [ `cat /proc/$i/cmdline` = %s ]; then echo $i; fi;done 2>/dev/null" % name).strip()
    print("getpid", out)
    if not out: return None
    return list(map(int, out.split('\n')))


def _get_pids_from_ps_output(output, name):
    """
    find process ids by name in ps output

    assuming format like
    `wifi         30849     1 0 06:06:08 ?     00:00:07 wpa_supplicant -O/data/vendor/wifi/wpa/sockets -puse_p2p_group_interface=1 -dd -g@android:vendor_wpa_wlan0`

    :param output: stdout content of ps
    :param name: target process name that being looking for
    :return: matched pids, in a list
    """
    ptn = re.compile(r'\S+\s+(?P<pid>\d+)\s+\S+\s+\d+\s+[\d:]+\s+\S+\s+\d\d:\d\d:\d\d\s+(?P<cmd>.*)')
    #print(output)
    lines = output.split('\n')
    header, body = lines[0], lines[1:]
    ret = []
    for line in body:
        matched = ptn.match(line)
        if not matched:
            logging.warning("ps line not match: %r" % line)
            continue
        gd = matched.groupdict()
        if gd['cmd'] == name:
            ret.append(int(gd['pid']))
    return ret


@maybe_restart_adb()
def get_pids(serial, name):
    out = gAdbClient.device(serial).shell("pidof '%s' 2>/dev/null" % name).strip()
    if out:
        ret = list(filter(None, out.strip().split()))
        if ret: return ret
    return []

# metrics

PROC_STAT_HEADERS = ["user", "nice", "system", "idle", "iowait", "irq", "softirq", "steal", "guest", "guest_nice"]
DEFAULT_STAT = dict(zip(PROC_STAT_HEADERS, [0] * (len(PROC_STAT_HEADERS) - 0)))


@maybe_restart_adb()
def get_cpu_stat(serial, pid=None):
    if pid is None:
        cmd = "cat /proc/stat 2>/dev/null"
    else:
        cmd = "cat /proc/%d/stat 2>/dev/null" % pid
    device = gAdbClient.device(serial)
    if not device:
        return None
    rows = device.shell(cmd).strip().split('\n')
    stats = []
    for row in rows:
        if row.startswith('cpu'):
            columns = list(zip(
                PROC_STAT_HEADERS,
            map(int, row.split()[1 : 1 + len(PROC_STAT_HEADERS)])
            ))
            if len(columns) < len(PROC_STAT_HEADERS):
                break
            stats.append(dict(columns))
        else:
            break
    return stats if stats else None

def _calc_cpu_usage(stat, prev_stat = None):
    """
    see:
        [1] https://stackoverflow.com/questions/23367857/accurate-calculation-of-cpu-usage-given-in-percentage-in-linux
        [2] http://www.linuxhowtos.org/System/procstat.htm
    :param stat:
    :param prev_stat: previous stat
    :return: cpu usage
    """
    if prev_stat is None:
        prev_stat = DEFAULT_STAT
    PrevIdle = prev_stat['idle'] + prev_stat['iowait']
    Idle = stat['idle'] + stat['iowait']

    PrevNonIdle = prev_stat['user'] + prev_stat['nice'] + prev_stat['system'] \
                  + prev_stat['irq'] + prev_stat['softirq'] + prev_stat['steal']
    NonIdle = stat['user'] + stat['nice'] + stat['system'] \
                + stat['irq'] + stat['softirq'] + stat['steal']

    PrevTotal = PrevIdle + PrevNonIdle
    Total = Idle + NonIdle

    totold = max(Total - PrevTotal + 1, 0.1)
    idled = Idle - PrevIdle + 1
    # the extra ONE is added to prevent div zero error

    CPU_Percentage = (totold - idled) * 100.0 / totold
    return CPU_Percentage

def calc_cpu_usage(stat, prev_stat = None):
    ret = 0
    if not stat:
        return 0
    #print(stat, prev_stat)
    for i in range(1, len(stat)): # skip the total cpu row
        ret += _calc_cpu_usage(stat[i], prev_stat[i] if (prev_stat and i < len(prev_stat)) else DEFAULT_STAT)
    return ret

@maybe_restart_adb()
def get_gpu_usage(serial):
    qcom = "cat /sys/class/kgsl/kgsl-3d0/gpubusy 2>/dev/null"
    mali = "cat /sys/kernel/debug/ged/hal/gpu_utilization 2>/dev/null"
    ret = gAdbClient.device(serial).shell(qcom + " || " + mali).strip().split()
    if len(ret) == 2: # qcom
        return int(ret[0]) * 100.0 / int(ret[1])
    if len(ret) == 3: # mali
        return (int(ret[0]) + int(ret[1])) * 100.0 / sum(map(int, ret))
    return 0

@maybe_restart_adb()
def is_root(serial):
    return check_file_exists(serial, "/system/app/Superuser.apk") \
            or check_file_exists(serial, "/sbin/su") \
            or check_file_exists(serial, "/system/bin/su") \
            or check_file_exists(serial, "/system/xbin/su") \
            or check_file_exists(serial, "/data/local/xbin/su") \
            or check_file_exists(serial, "/data/local/bin/su") \
            or check_file_exists(serial, "/system/sd/xbin/su") \
            or check_file_exists(serial, "/system/bin/failsafe/su") \
            or check_file_exists(serial, "/data/local/su") \
            or check_file_exists(serial, "/su/bin/su")

@maybe_restart_adb()
def enable_tcpip(serial, port):
    ret = gAdbClient.device(serial).tcpip(port)
    if ret:
        status, message = ret
        logger.info("enable_tcpip(%s, %s) => %s, %s ", serial, port, status, message)
        return bool(status)

@maybe_restart_adb()
def disable_tcpip(serial):
    ret = gAdbClient.device(serial).usb()
    if ret:
        status, message = ret
        logger.info("disable_tcpip(%s) => %s, %s ", serial, status, message)
        return bool(status)

@maybe_restart_adb()
def wait_for_device(serial, timeout=10):
    ret = None
    timeleft = timeout
    while 1:
        ret = gAdbClient.device(serial)
        if ret: break
        if timeleft < 0 and timeout > 0:
            break
        time.sleep(1)
        timeleft -= 1
    return ret

@maybe_restart_adb()
def connect(host, port):
    ret = gAdbClient.connect(host, port)
    if ret:
        status, message = ret
        logger.info("connect(%s, %s) => %s, %s ", host, port, status, message)
        return bool(status)

@maybe_restart_adb()
def disconnect(host, port):
    ret = gAdbClient.disconnect(host, port)
    if ret:
        status, message = ret
        logger.info("disconnect(%s, %s) => %s, %s ", host, port, status, message)
        return bool(status)

def check_file_exists(serial, path):
    sync_conn = gAdbClient.device(serial).sync()
    sync = Sync(sync_conn)
    sync._send_str(Protocol.STAT, path)
    ret = sync_conn.read(1024)
    sync_conn.close()
    # print("stat return: ", ret)
    if len(ret) != 12 + 4: return False
    mode, size, mtime = struct.unpack('<III', ret[4:])
    # print("mode =", mode, "size = ", size, "mtime = ", mtime)
    return mtime != 0


@maybe_restart_adb()
def is_debuggable(serial, package):
    ret = gAdbClient.device(serial).shell("run-as %s" % package).strip().split()
    return "not debuggable" not in ret

# Perf
@maybe_restart_adb()
def enable_perf(serial):
    gAdbClient.device(serial).shell("setprop security.perf_harden 0")
    print("security.perf_harden = ", gAdbClient.device(serial).shell("getprop security.perf_harden"))

@maybe_restart_adb()
def get_perf_harden(serial):
    return gAdbClient.device(serial).shell("getprop security.perf_harden").strip()

@maybe_restart_adb()
def get_mem_usage(serial, package_name, summary = True):
    out = gAdbClient.device(serial).shell("dumpsys meminfo %s 2>/dev/null" % package_name).strip()
    if summary:
        total_pss = 0
        native_heap = 0
        if out:
            match = re.search(r'TOTAL[^\d]+(\d+)', out)
            if match:
                total_pss = match.group(1)
            match = re.search(r'Native Heap[^\d]+(\d+)', out)
            if match:
                native_heap = match.group(1)
        return total_pss, native_heap
    return out

@maybe_restart_adb()
def forward(serial, local, remote):
    return gAdbClient.device(serial).forward(local, remote, norebind=True)

@maybe_restart_adb()
def killforward(serial, local):
    return gAdbClient.device(serial).killforward(local)

@maybe_restart_adb()
def screencap(serial, output_file):
    temp_file = "/data/local/tmp/" + os.path.basename(output_file)
    out = gAdbClient.device(serial).shell("screencap %s" % temp_file).strip()
    gAdbClient.device(serial).pull(temp_file, output_file)

class UnixSockConn:
    def __init__(self, serial, name):
        self.serial = serial
        self.name = name
        self.conn = None

    def __enter__(self):
        print("...................... __enter__ ..")
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("...................... exit ..")
        self.disconnect()
        pass

    def connect(self):
        port = random.randint(50000, 60000)
        self.device = gAdbClient.device(self.serial)
        self.serial = self.serial
        self.port = port
        self.local = "tcp:{}".format(port)
        self.remote = "localabstract:{}".format(self.name)
        self.device.forward(self.local, self.remote, norebind=True)
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect(("127.0.0.1", self.port))

    def is_connected(self):
        return self.conn is not None and self.conn.fileno() != -1

    def disconnect(self):
        self.conn.close()
        self.conn = None
        self.device.killforward(self.local)

    def send(self, buf):
        return self.conn.send(buf)

    def recv(self, len):
        #print("...................... recv ..")
        return self.conn.recv(len)

def run_as(serial, package, cmd):
    def handler(conn):
        conn.send(cmd + '\n')
        print(conn.read(1024))
        conn.close()
    gAdbClient.device(serial).shell("run-as " + package, handler)