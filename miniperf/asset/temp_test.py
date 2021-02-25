from u3driver import AltrunUnityDriver
from u3driver import By
import time
import argparse

def AutoRun(udriver):
	try:
		udriver.find_object(By.PATH,"//UICamera//Loadout//OpenLeaderboard").tap()
		time.sleep(2.266979)
		udriver.find_object(By.PATH,"//UICamera//Leaderboard//Background//Button").tap()
		time.sleep(1.701202)
		udriver.find_object(By.PATH,"//UICamera//Loadout//StoreButton").tap()
		time.sleep(2.167458)
		udriver.find_object(By.PATH,"//Canvas//Background//Button").tap()
		time.sleep(1.500839)
		udriver.find_object(By.PATH,"//UICamera//Loadout//MissionButton").tap()
		time.sleep(2.100597)
		udriver.find_object(By.PATH,"//UICamera//Loadout//MissionPopup//MissionBackground//CloseButton").tap()
		time.sleep(1.900288)
		udriver.find_object(By.PATH,"//UICamera//Loadout//SettingButton").tap()
		time.sleep(3.301136)
		udriver.find_object(By.PATH,"//UICamera//Loadout//SettingPopup//Background//About").tap()
		time.sleep(1.46693)
		udriver.find_object(By.PATH,"//UICamera//Loadout//SettingPopup//AboutPopup//Image//BackButton").tap()
		time.sleep(1.900654)
		udriver.find_object(By.PATH,"//UICamera//Loadout//SettingPopup//Background//CloseButton").tap()
		time.sleep(2.166748)
		udriver.find_object(By.PATH,"//UICamera//Loadout//StartButton").tap()
		time.sleep(7.036194)
		udriver.find_object(By.PATH,"//UICamera//Game//WholeUI//pauseButton").tap()
		time.sleep(2.400276)
		udriver.find_object(By.PATH,"//UICamera//Game//PauseMenu//Exit").tap()
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