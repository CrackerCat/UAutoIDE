from u3driver import AltrunUnityDriver
from u3driver import By
import time
import argparse

def AutoRun(udriver):
	try:
		time.sleep(1.469812)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole2").tap()
		time.sleep(0.4010525)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole1").tap()
		time.sleep(0.3842049)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole3").tap()
		time.sleep(0.3521881)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole4").tap()
		time.sleep(0.4007244)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole5").tap()
		time.sleep(0.3666687)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole6").tap()
		time.sleep(0.368721)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole7").tap()
		time.sleep(0.3497047)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole8").tap()
		time.sleep(0.384716)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole9").tap()
		time.sleep(0.2839317)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole10").tap()
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