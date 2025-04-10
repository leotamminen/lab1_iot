import time
import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
URL = f"http://130.232.102.97:9090/api/v1/{ACCESS_TOKEN}/telemetry"
HEADERS = {
    "Content-Type": "application/json"
}

while True:
    payload = {
        "temperature": 42,
        "humidity": 73
    }
    response = requests.post(URL, headers=HEADERS, data=json.dumps(payload))
    print("HTTP status:", response.status_code, "| Data sent:", payload)
    time.sleep(5)
