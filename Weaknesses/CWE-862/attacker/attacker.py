import requests

url = "http://localhost:5000/api/device/on"
response = requests.post(url)

print(f"[*] Server response: {response.text}")
