from ruuvitag_sensor.ruuvi import RuuviTagSensor

class Ruuvitag(object):
	def __init__(self, macs, callback):
		RuuviTagSensor.get_datas(callback)
