from u3driver import AltrunUnityDriver
from u3driver import By
import time
import argparse

def AutoRun(udriver):
	try:
		time.sleep(1.254883)
		udriver.find_object(By.PATH,"//Canvas//Button").tap()
		time.sleep(0.2998047)
		udriver.find_object(By.PATH,"//Canvas//Button").tap()
		time.sleep(0.2841797)
		udriver.find_object(By.PATH,"//Canvas//Button").tap()
		time.sleep(0.2495117)
		udriver.find_object(By.PATH,"//Canvas//Button").tap()
		time.sleep(0.2475586)
		udriver.find_object(By.PATH,"//Canvas//Button").tap()
	except Exception as e:
		print(f'{e}')
		raise e

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-s', help="device serial")
	parser.add_argument('-i', help="ip address")
	parser.add_argument('-port', help="ip address")
	args = parser.parse_args()
	device_s = args.s
	ip = args.i
	port = int(args.port)
	udriver = AltrunUnityDriver(device_s,"", ip, TCP_PORT=port,timeout=60, log_flag=True)
	AutoRun(udriver)
	udriver.stop()