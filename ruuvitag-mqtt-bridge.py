import os
import json
from mqtt import MQTTClient
from ruuvitag import getMeasurements
from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
	mqtt_client = MQTTClient(os.getenv('MQTT_CLIENT_ID'))
	mqtt_client.connect(os.getenv('MQTT_BROKER_HOST'), int(os.getenv('MQTT_BROKER_PORT')))
	ruuvitag_macs = os.getenv('RUUVITAG_MACS').split(',')

	while True:
		for mac in ruuvitag_macs:
			measurements = getMeasurements(mac)
			mqtt_topic = 'ruuvitag/' + mac.replace(':', '')
			mqtt_client.publish(mqtt_topic, json.dumps(measurements))
		mqtt_client.loop()
