import requests
import time

# 🚨 Hardcoded credentials (vulnerability)
USERNAME = "admin"
PASSWORD = "123456"

# Server URL
API_URL = "http://server:5000/upload"

def send_sensor_data():
    sensor_data = {
        "device_id": "iot-001",
        "temperature": 22.5,
        "humidity": 60
    }

    response = requests.post(API_URL, json=sensor_data, auth=(USERNAME, PASSWORD))

    if response.status_code == 200:
        print("✅ Data sent successfully.")
    else:
        print("❌ Error:", response.text)

if __name__ == "__main__":
    while True:
        send_sensor_data()
        time.sleep(5)  # Send data every 5 seconds
