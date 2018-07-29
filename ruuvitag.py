import sys
from ruuvitag_sensor.ruuvitag import RuuviTag

def getMeasurement(mac):
	sensor = RuuviTag(mac)
	state = sensor.update()
	return sensor.state

if __name__ == '__main__':
	for mac in sys.argv[1:]:
		print(getMeasurement(mac))
