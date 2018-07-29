import os
from mqtt import MQTTClient
from ruuvitag import getMeasurements
from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
	mqtt_client = MQTTClient(os.getenv('MQTT_CLIENT_ID'))
	mqtt_client.connect(os.getenv('MQTT_BROKER_HOST'), int(os.getenv('MQTT_BROKER_PORT')))
	ruuvitag_macs = os.getenv('RUUVITAG_MACS').split(',')
	publish_measurements = ['humidity', 'pressure', 'temperature', 'battery']

	while True:
		for mac in ruuvitag_macs:
			for measurement in publish_measurements:
				measurements = getMeasurements(mac)
				if measurement in measurements:
					mqtt_topic = 'ruuvitag/' + mac.replace(':', '') + '/' + measurement
					mqtt_client.publish(mqtt_topic, str(measurements[measurement]))
