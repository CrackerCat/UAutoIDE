from u3driver import AltrunUnityDriver
from u3driver import By
import time
import argparse

def AutoRun(udriver):
	try:
		time.sleep(1.499985)
		udriver.find_object(By.PATH,"//Canvas//StartButton").tap()
		time.sleep(1.900574)
		udriver.find_object(By.PATH,"//UICamera//Loadout//OpenLeaderboard").tap()
		time.sleep(1.066669)
		udriver.find_object(By.PATH,"//UICamera//Leaderboard//Background//Button").tap()
		time.sleep(0.6998367)
		udriver.find_object(By.PATH,"//UICamera//Loadout//StoreButton").tap()
		time.sleep(0.7669754)
		udriver.find_object(By.PATH,"//Canvas//Background//Button").tap()
		time.sleep(0.5999718)
		udriver.find_object(By.PATH,"//UICamera//Loadout//MissionButton").tap()
		time.sleep(0.7333908)
		udriver.find_object(By.PATH,"//UICamera//Loadout//MissionPopup//MissionBackground//CloseButton").tap()
		time.sleep(0.6330109)
		udriver.find_object(By.PATH,"//UICamera//Loadout//SettingButton").tap()
		time.sleep(0.633503)
		udriver.find_object(By.PATH,"//UICamera//Loadout//SettingPopup//Background//CloseButton").tap()
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