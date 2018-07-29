import sys
from ruuvitag_sensor.ruuvitag import RuuviTag

def getMeasurements(mac):
	sensor = RuuviTag(mac)
	state = sensor.update()
	return sensor.state

