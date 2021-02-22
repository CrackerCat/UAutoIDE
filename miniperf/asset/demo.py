from u3driver import AltrunUnityDriver
from u3driver import By
import time
import argparse

def AutoRun(udriver):
	try:
		time.sleep(1.871627)
		udriver.find_object(By.PATH,"//Canvas//StartButton").tap()
		time.sleep(7.936314)
		udriver.find_object(By.PATH,"//UICamera//Loadout//OpenLeaderboard").tap()
		time.sleep(1.988369)
		udriver.find_object(By.PATH,"//UICamera//Leaderboard//Background//Button").tap()
		time.sleep(1.069744)
		udriver.find_object(By.PATH,"//UICamera//Loadout//StoreButton").tap()
		time.sleep(1.687033)
		udriver.find_object(By.PATH,"//Canvas//Background//Button").tap()
		time.sleep(0.9031086)
		udriver.find_object(By.PATH,"//UICamera//Loadout//MissionButton").tap()
		time.sleep(1.085651)
		udriver.find_object(By.PATH,"//UICamera//Loadout//MissionPopup//MissionBackground//CloseButton").tap()
		time.sleep(0.7683506)
		udriver.find_object(By.PATH,"//UICamera//Loadout//SettingButton").tap()
		time.sleep(0.9359722)
		udriver.find_object(By.PATH,"//UICamera//Loadout//SettingPopup//Background//CloseButton").tap()
		time.sleep(2.60672)
		udriver.find_object(By.PATH,"//UICamera//Loadout//StartButton").tap()
		time.sleep(6.49966)
		udriver.find_object(By.PATH,"//UICamera//Game//WholeUI//pauseButton").tap()
		time.sleep(1.369797)
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