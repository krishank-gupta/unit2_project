import requests
from datetime import datetime
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
gpios = [4,27,22,23]

# new_user = {
#     "username": "Krish&Thumula",
#     "password": "420deeznuts69"
# }

# req = requests.post("http://192.168.6.142/register", json=new_user)

# print(req.json())

user = {
    "username": "Krish&Thumula",
    "password": "420deeznuts69"
}

req = requests.post('http://192.168.6.142/login', json=user)
access_token = req.json()["access_token"]

auth = {
    "Authorization": f"Bearer {access_token}"
}

print(auth)

# for i in range(1, 5, 1):

#     temp_hum = {
#         "name": f"Krish&Thumula Hum{i}",
#         "unit": "%",
#         "location": "R1-14B",
#         "type": "Humditiy"
#     }
#     temp_temp = {
#         "name": f"Krish&Thumula Temp{i}",
#         "unit": "C",
#         "location": "R1-14B",
#         "type": "Temperature"
#     }

#     temp_req = requests.post('http://192.168.6.142/sensor/new', json=temp_temp, headers=auth)
#     hum_req = requests.post('http://192.168.6.142/sensor/new', json=temp_hum, headers=auth)

#     print(temp_req.json())
#     print(hum_req.json())

server_sensors_list = (requests.get("http://192.168.6.142/sensors", headers=auth).json())



while True:
    for i in range(0, 4,1):
        humidity, temperature = Adafruit_DHT.read_retry(sensor, gpios[i])
    
        if (humidity is not None and temperature is not None):
            print('Sensor', {i+1},': Temp={0:0.1f}C Humidity={1:0.1f}%'.format(temperature, humidity))

            # main
            for i in ((server_sensors_list['readings'][0])):
                if i['id'] in range(15,23,2):
                    print(i)

                    new_record ={"datetime":datetime.isoformat(datetime.now()),"sensor_id":i['id'], "value":temperature}

                    r = requests.post('http://192.168.6.142/reading/new', json=new_record, headers=auth)
                    print(r.json())
                
                if i['id'] in range(16,23,2):
                    print(i)

                    new_record ={"datetime":datetime.isoformat(datetime.now()),"sensor_id":i['id'], "value":humidity}

                    r = requests.post('http://192.168.6.142/reading/new', json=new_record, headers=auth)
                    print(r.json())
                
        else:
            print('Failed to get reading. Try again!')
    time.sleep(60)

    


# ruben_data = requests.get("http://192.168.6.142/readings")

# ruben_data = ruben_data.json()
# ruben_data = ruben_data['readings'][0]

# for i in range(0, len(ruben_data),1):
#     if ruben_data[i]['sensor_id'] == 4:
#         print(ruben_data[i]['value'], '%')
#     if ruben_data[i]['sensor_id'] == 5:
#         print(ruben_data[i]['value'], 'C')


