import os
import json
from mqtt import MQTTClient
from ruuvitag import getMeasurement
from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
	mqtt_client = MQTTClient(os.getenv('MQTT_CLIENT_ID'))
	mqtt_client.connect(os.getenv('MQTT_BROKER_HOST'), int(os.getenv('MQTT_BROKER_PORT')))
	ruuvitag_macs = os.getenv('RUUVITAG_MACS').split(',')

	for mac in ruuvitag_macs:
		mqtt_topic = 'ruuvitag/' + mac.replace(':', '')
		measurement = getMeasurement(mac)
		print(measurement)
		mqtt_client.publish(mqtt_topic, json.dumps(measurement))
