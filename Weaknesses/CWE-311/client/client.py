import requests
import time

SERVER_URL = "http://127.0.0.1:5620/data"

while True:
    data = {"temperature": 25, "device_id": "iot-001"}
    response = requests.post(SERVER_URL, json=data)
    print(f"Sent data: {data}, Response: {response.status_code}")
    time.sleep(5)
