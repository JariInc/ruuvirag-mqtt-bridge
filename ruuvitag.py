import sys
import logging
from ruuvitag_sensor.ruuvitag import RuuviTag

log = logging.getLogger('ruuvitag-mqtt-bridge.ruuvitag')

def getMeasurements(mac):
	log.debug('Waiting %s', mac)
	sensor = RuuviTag(mac)
	state = sensor.update()
	log.debug('%s returned %s', mac, state)

	return sensor.state
