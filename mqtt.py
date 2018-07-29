import paho.mqtt.client as mqtt

class MQTTClient(object):
	def  __init__(self, client_id):
		self.client_id = client_id

	def connect(self, address, port):
		self.client = mqtt.Client(self.client_id)
		self.client.connect(address, port)

	def publish(self, topic, payload):
		self.client.publish(topic, payload)
