from u3driver import AltrunUnityDriver
from u3driver import By
import time
import argparse

def AutoRun(udriver):
	try:
		time.sleep(2.421875)
		udriver.find_object(By.PATH,"//UIModule//Group1//UILoginChannelInner//imgBG//btnEnterGame").tap()
		time.sleep(1.054688)
		udriver.find_object(By.PATH,"//UIModule//Group1//UILoginServer//imgBG//btnLoginServer").tap()
		time.sleep(2.007813)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole6").tap()
		time.sleep(0.4296875)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole4").tap()
		time.sleep(0.3984375)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole2").tap()
		time.sleep(0.7734375)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole8").tap()
		time.sleep(0.3203125)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole7").tap()
		time.sleep(0.328125)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole5").tap()
		time.sleep(0.2890625)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole3").tap()
		time.sleep(0.328125)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole4").tap()
		time.sleep(0.3359375)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole6").tap()
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