# Import libraries
import requests
from datetime import datetime
import time
import Adafruit_DHT
from library import user_signup, create_sensors, get_auth, post_record

# Initializa Adafruit
sensor = Adafruit_DHT.DHT11

# List of gpio pins on rasberry
gpios = [4,27,22,23]

new_user = {
    "username": "Krish&Thumula",
    "password": "#############"
}

# Create the new user
# user_signup(new_user=new_user)

user = {
    "username": "Krish&Thumula",
    "password": "#############"
}

# Create sensors for the user:
create_sensors(get_auth(user))

while True:
    for x in range(0, 4,1):
        # Get Auth
        auth = (get_auth(user))
        humidity, temperature = Adafruit_DHT.read_retry(sensor, gpios[x])
        server_sensors_list = (requests.get("http://192.168.6.142/sensors", headers=auth).json())

        if (humidity is not None and temperature is not None):
            print('Sensor', {x+1},': Temp={0:0.1f}C Humidity={1:0.1f}%'.format(temperature, humidity))
            
            # Post data
            post_record('temperature', temperature, x, get_auth(user))
            post_record('humidity', humidity, x, get_auth(user))    

        else:
            print('Failed to get reading. Try again!')
    time.sleep(300)
