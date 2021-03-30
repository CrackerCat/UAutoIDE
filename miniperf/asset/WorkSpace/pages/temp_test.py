from u3driver import AltrunUnityDriver
from u3driver import By
import time
import argparse

def AutoRun(udriver):
	try:
		time.sleep(0.9367523)
		udriver.find_object(By.PATH,"//Canvas//Button").tap()
		time.sleep(0.2160797)
		udriver.find_object(By.PATH,"//Canvas//Button").tap()
		time.sleep(0.1787872)
		udriver.find_object(By.PATH,"//Canvas//Button").tap()
		time.sleep(0.1789246)
		udriver.find_object(By.PATH,"//Canvas//Button").tap()
		time.sleep(0.1781311)
		udriver.find_object(By.PATH,"//Canvas//Button").tap()
		time.sleep(0.719986)
		udriver.find_object(By.PATH,"//Canvas//Button (1)").tap()
		time.sleep(0.2126465)
		udriver.find_object(By.PATH,"//Canvas//Button (1)").tap()
		time.sleep(0.1801453)
		udriver.find_object(By.PATH,"//Canvas//Button (1)").tap()
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