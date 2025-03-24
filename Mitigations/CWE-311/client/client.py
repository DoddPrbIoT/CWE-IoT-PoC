import requests
import time

SERVER_URL = "https://server/data"

while True:
    data = {"temperature": 25, "device_id": "iot-001"}
    response = requests.post(SERVER_URL, json=data, verify="./ssl.crt")
    
    print(f"Sent data securely: {data}, Response: {response.status_code}")
    time.sleep(5)
