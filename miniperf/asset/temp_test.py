from u3driver import AltrunUnityDriver
from u3driver import By
import time
import argparse

def AutoRun(udriver):
	try:
		time.sleep(1.969818)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole1").tap()
		time.sleep(0.6347961)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole3").tap()
		time.sleep(0.5344238)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole5").tap()
		time.sleep(0.7349854)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole7").tap()
		time.sleep(0.818573)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole9").tap()
		time.sleep(0.8843994)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole2").tap()
		time.sleep(0.4173889)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole4").tap()
		time.sleep(0.3840332)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole6").tap()
		time.sleep(0.3674927)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole8").tap()
		time.sleep(1.686523)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole10").tap()
		time.sleep(1.385315)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//btnMale2").tap()
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