import logging
import paho.mqtt.client as mqtt

class MQTTClient(object):
	keepalive = 60

	def  __init__(self, client_id):
		self.client_id = client_id

	def connect(self, address, port):
		self.client = mqtt.Client(self.client_id)
		self.client.enable_logger(logging.getLogger('ruuvitag-mqtt-bridge.mqtt'))
		self.client.connect(address, port, self.keepalive)
		self.client.reconnect_delay_set(5, 600)

	def publish(self, topic, payload):
		self.client.publish(topic, payload)

	def loop(self):
		self.client.loop()
