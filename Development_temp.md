### Create new sensors
```.py
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
```

This function is designed to create four sensors in the server. First there is a for loop that will loop for four times and each time the loop is run, there will be  two temporary dictionaries created, and in the dictionaries it contains the name, the unit, the location and the type of each sensor. And after the dictionaries are  created the dictionaries are converted to JSON and then posted to http://192.168.6.142/sensor/new. And finally the function gives out the sensor id of the newly uploaded sensors' id and owner's id with details that were given when sensors were being uploaded to the server( name, unit, location and type).

### Get authrization key

```.py
def get_auth(user, url="http://192.168.6.142"):
    req = requests.post(f"{url}/login", json=user)
    access_token = req.json()['access_token']
    auth = {"Authorization": f"Bearer {access_token}"}
    return auth
```

Purpose of this function is to get the authorization key from the server. The username and the password are inputted as a dictionary(user) to the function. Using the request library, the username and the password is sent to the server using post. Then then the access token is taken and converted using JSON. And then the access token is stored in a dictionary called auth and the key for the token is Authorization. Finally the function returns the dictionary auth.

### Get data from the server

```.py
def get_data(id):
    # Get data from server
    response = requests.get("http://192.168.6.142/readings")
    data = response.json()
    data_all = data['readings'][0]
    
    # Init empty list to append data 
    output = []
    
    # For every item in data
    for i in range(0, len(data), 1):
        # If item matches required ID, append to output list
        if data[i]['sensor_id'] == id:
            output.append(data[i]['value'])
    
    # Return output list
    return output
```
    
This function can be used to get the readings from the registered sensors in "http://192.168.6.142". First the id of the sensor that the data is given is inputted as id. Then the function gets data from "http://192.168.6.142/readings" and then converts the data as JSON and is stored in the variable data. The readings of sensors are stored as data_all. Then the output list is created which is empty. Then for every item in data_all the program checks if the "sensor_id" is the same as id that was inputted at the beginning of the function. And if the "sensor_id" matches with the id the readings of the sensor(which is stored in the key "value") is appended to the output list. After the loop is completed the function returns the output list.
