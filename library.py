import requests
from datetime import datetime

url = "http://192.168.6.142/"

def user_signup(new_user):
    req = requests.post(f"{url}register", json=new_user)
    return req.json()

def create_sensors(auth):
    for i in range(1, 5, 1):
        temp_hum = {
            "name": f"Krish&Thumula Hum{i}",
            "unit": "%",
            "location": "R1-14B",
            "type": "Humditiy"
        }
        temp_temp = {
            "name": f"Krish&Thumula Temp{i}",
            "unit": "C",
            "location": "R1-14B",
            "type": "Temperature"
        }

        temp_req = requests.post('http://192.168.6.142/sensor/new', json=temp_temp, headers=auth)
        hum_req = requests.post('http://192.168.6.142/sensor/new', json=temp_hum, headers=auth)

        print(temp_req.json())
        print(hum_req.json())

def get_auth(user):
    req = requests.post(f"{url}/login", json=user)
    access_token = req.json()['access_token']
    auth = {"Authorization": f"Bearer {access_token}"}
    print(auth)
    return auth

def post_record(type, value, x, auth):
    humIds = [15,17,19,21]
    tempIds = [16,18,20,22]
    
    if type == 'temperature':
        new_record = {
            "datetime":datetime.isoformat(datetime.now()),
            "sensor_id": tempIds[x], 
            "value":value
        }
        r = requests.post('http://192.168.6.142/reading/new', json=new_record, headers=auth)

        print(r.json())

    if type == 'humidity':
        new_record = {
            "datetime":datetime.isoformat(datetime.now()),
            "sensor_id": humIds[x], 
            "value":value
        }
        r = requests.post('http://192.168.6.142/reading/new', json=new_record, headers=auth)
        print(r.json())

def get_data(id):
    # Get data from server
    response = requests.get("http://192.168.6.142/readings")
    data = response.json()
    data = data['readings'][0]
    
    # Init empty list to append data 
    output = []
    
    # For every item in data
    for i in range(0, len(data), 1):
        # If item matches required ID, append to output list
        if data[i]['sensor_id'] == id:
            output.append(data[i]['value'])
    
    # Return output list
    return output
