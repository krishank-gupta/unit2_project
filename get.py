# Import libraries
import requests
from datetime import datetime

user = {
    "username": "Krish&Thumula",
    "password": "420deeznuts69"
}

req = requests.post('http://192.168.6.142/login', json=user)
access_token = req.json()["access_token"]

auth = {"Authorization": f"Bearer {access_token}"}

print(auth)


response = requests.get("http://192.168.6.142/readings")

data = response.json()
data = data['readings'][0]

for i in range(0, len(data), 1):
    if data[i]['sensor_id'] in range(15,23,1):
        print(data[i])
