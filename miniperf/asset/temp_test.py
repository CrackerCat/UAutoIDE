from u3driver import AltrunUnityDriver
from u3driver import By
import time
import argparse

def AutoRun(udriver):
	try:
		time.sleep(1.168671)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//PanelCreateRole//btnRandRoleName").tap()
		time.sleep(0.3341064)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//PanelCreateRole//btnRandRoleName").tap()
		time.sleep(0.1838074)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//PanelCreateRole//btnRandRoleName").tap()
		time.sleep(0.1665039)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//PanelCreateRole//btnRandRoleName").tap()
		time.sleep(0.1671143)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//PanelCreateRole//btnRandRoleName").tap()
		time.sleep(0.3007507)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//PanelCreateRole//btnRandRoleName").tap()
		time.sleep(2.436951)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//PanelCreateRole//btnRandRoleName").tap()
		time.sleep(0.150177)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//PanelCreateRole//btnRandRoleName").tap()
		time.sleep(0.1673889)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//PanelCreateRole//btnRandRoleName").tap()
		time.sleep(0.1836548)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//PanelCreateRole//btnRandRoleName").tap()
		time.sleep(0.1667175)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//PanelCreateRole//btnRandRoleName").tap()
		time.sleep(0.1835022)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//PanelCreateRole//btnRandRoleName").tap()
		time.sleep(0.1506958)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//PanelCreateRole//btnRandRoleName").tap()
		time.sleep(1.752441)
		udriver.find_object(By.PATH,"//UIModule//Group1//UISelectRole//imgBG//btnFemale2").tap()
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