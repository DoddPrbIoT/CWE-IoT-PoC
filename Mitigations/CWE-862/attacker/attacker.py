import requests

url = "http://localhost:5000/api/login"
device_url = "http://localhost:5000/api/device/on"

response = requests.post(url, json={
    "username": "admin", 
    "password": "admin"
}, headers={
    "Content-Type": "application/json"
})


if response.status_code == 200:
    data = response.json()
    access_token = data['access_token']
    print(f"[*] Access token: {data['access_token']}") 
    
    # Connection to device
    device_response = requests.post(device_url,headers={
        "Authorization": f'Bearer {access_token}'
    })
    
    if(device_response.status_code == 200):
        print(f"[*] Connection established")
        print(device_response.json())
    else:
        print("Connection refused")
        
else:
    print(f"[!] Error {response.status_code}: {response.text}")
