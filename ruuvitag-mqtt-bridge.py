import os
import json
import logging
from mqtt import MQTTClient
from ruuvitag import getMeasurements
from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':

	logger = logging.getLogger('ruuvitag-mqtt-bridge')
	logger.setLevel(logging.DEBUG)
	ch = logging.StreamHandler()
	ch.setLevel(logging.INFO)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	ch.setFormatter(formatter)
	logger.addHandler(ch)

	logger.info("Starting app")

	mqtt_client = MQTTClient(os.getenv('MQTT_CLIENT_ID'))
	mqtt_client.connect(os.getenv('MQTT_BROKER_HOST'), int(os.getenv('MQTT_BROKER_PORT')))
	ruuvitag_macs = os.getenv('RUUVITAG_MACS').split(',')

	logger.info("Listening ruuvitags %s", ruuvitag_macs);

	while True:
		for mac in ruuvitag_macs:
			measurements = getMeasurements(mac)
			mqtt_topic = 'ruuvitag/' + mac.replace(':', '')
			logger.info("Publishing %s", mac)
			mqtt_client.publish(mqtt_topic, json.dumps(measurements))
			mqtt_client.loop()
