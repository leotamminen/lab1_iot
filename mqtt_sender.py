import time
import json
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os

load_dotenv()

BROKER = "130.232.102.97"
PORT = 1884
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
TOPIC = "v1/devices/me/telemetry"

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(BROKER, PORT)

while True:
    payload = {
        "temperature": 42,
        "humidity": 73
    }
    client.publish(TOPIC, json.dumps(payload))
    print("MQTT data sent:", payload)
    time.sleep(5)
