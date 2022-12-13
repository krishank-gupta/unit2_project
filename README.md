![overview](https://user-images.githubusercontent.com/50672613/207326246-4b9b538a-956b-4607-a67f-f748aaf02b8b.gif)

# Unit 2: A Distributed Weather Station for ISAK

## Criteria A: Planning

## Problem definition
A teacher at a local school wants to start a marijuana farm. He wants a software that will tell him the temperature of his farm and his dormitory room where he keeps the harvested marijuana in. He wants to make sure that the marijuana is in the ideal temperature for growth and for storage. He wants adequate precision because marijuana needs specific temperature and humidity to grow or it will die. The temperature of the farm and storage rooms are controlled so that the temperature range will always be between 0° and 50°C and the humidity will always be between 20% and 90%. After getting the temperature and humidity data, the teacher will manually change his heaters and humidifiers. He wants the software to predict the temperature and humidity for the next 12 hours so that if he needs to change the heater and humidifier settings, he can be prepared. Since it is a small business that's just starting, he wants to keep the costing to a minimum. 

## Proposed Solution
Considering the client requirements an adequate solution includes a low cost sensing device for humidity and temperature and a custom data script that process and anaysis the samples acquired. For a low cost sensing device an adequate alternative is the DHT11 sensor[^1] which is offered online for less than 5 USD and provides adequare precision and range for the client requirements (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). Similar devices such as the DHT22, AHT20 or the AM2301B [^2] have higher specifications, however the DHT11 uses a simple serial communication (SPI) rather than more eleborated protocols such as the I2C used by the alternatives. For the range, precision and accuracy required in this applicaiton the DHT11 provides the best compromise. Connecting the DHT11 sensor to a computer requires a device that provides a Serial Port communication. A cheap and often used alternative for prototyping is the Arduino UNO microcontroller [^3]. "Arduino is an open-source electronics platform based on easy-to-use hardware and software"[^4]. In additon to the low cost of the Arduino (< 6USD), this devide is programable and expandable[^1]. Other alternatives include diffeerent versions of the original Arduino but their size and price make them a less adequate solution.

Considering the budgetary constrains of the client and the hardware requirements, the software tool that I proposed for this solution is Python. Python is open source, it is mature and supported in mutiple platforms (platform-independent) including macOS, Windows, Linux and can also be used to program the Arduino microprocessor [^5][^6]. In comparison to the alternative C or C++, which share similar features, Python is a High level programming language (HLL) with high abstraction [^7]. For example, memory management is automatic in Python whereas it is responsability of the C/C++ developer to allocate and free up memory [^7], this could result in faster applications but also memory problems. In addition a HLL language will allow me and future developers extend the solution or solve issues proptly.  

**Design statement**

[^1]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 
[^2]: Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.   
[^3]:“How to Connect dht11 Sensor with Arduino Uno.” Arduino Project Hub, https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239.  
[^4]:Team, The Arduino. “What Is Arduino?: Arduino Documentation.” Arduino Documentation | Arduino Documentation, https://docs.arduino.cc/learn/starting-guide/whats-arduino.  
[^5]:Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability Query Is Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata. 
[^6]:Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/. 
[^7]: Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management. 
## Success Criteria

1. The solution provides a visual representation of the Humidity and Temperature values inside a dormitory (Local) and outside the house (Remote) for a period of minimum 48 hours. 
1. ```[HL]``` The local variables will be measure using a set of 4 sensors around the dormitory.
2. The solution provides a mathematical modelling for the Humidity and Temperature levels for each Local and Remote locations. ```(SL: linear model)```, ```(HL: non-lineal model)```
3. The solution provides a comparative analysis for the Humidity and Temperature levels for each Local and Remote locations including mean, standad deviation, minimum, maximum, and median.
4. ```(SL)```The Local samples are stored in a csv file and ```(HL)``` posted to the remote server.
5. Create a prediction the subsequent 12 hours for both temperature and humidity.
6. A poster summarizing the visual representations, model and analysis is created. The poster includes a recommendation about healthy levels for Temperature and Humidity.

# Criteria B: Design

## System Diagram
![](https://github.com/krishank-gupta/unit2_project/blob/main/sysdim_hl.png.png)

**Fig.1:** This shows the system diagram for the proposed solution (**HL**). The indoor variables will be measured using a Raspberry PI and four DHT11 sensors located inside a room. Four sensors are used to determine more precisely the physical values and include measurement uncertainty. The outdoor variables will be requested to the remote server using a GET request to the API of the server at ```192.168.6.147/readings```. The local values are stored in a CSV database locally and POST to the server using the API and TOKEN authentication. A laptop computer is used for remotely controlling the local Rasberry Pi using a Dekptop sharing application (VNC Viewer). (Optional) Data from the local raspberry is downloaded to the laptop for analysis and processing.

## Flow Diagrams
### Registering a new user
![](https://github.com/krishank-gupta/unit2_project/blob/main/New_user_%20flow_diagram.png)

**Fig.2:** Flow diagram for the new user registration function

### Adding four new sensors to the server
![](https://github.com/krishank-gupta/unit2_project/blob/main/New_sensor_diagram.png)

**Fig.3** Flow diagram for adding four new sensors to the server

### Getting readings from server
![](https://github.com/krishank-gupta/unit2_project/blob/main/Get_readings_diagram.png)

**Fig.4** Flow diagram for getting readings from the server for a specific sensor id.

## Record of Tasks
| Task No | Planned Action                                     | Planned outcome                                                                                        | Time estimate | Target completion date | Criterion |
|---------|----------------------------------------------------|--------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Write the problem definition                       | Have a problem definition matching with the proposed solution                                          | 10 min        | Dec 03                 | A         |
| 2       | Planning how the circuit should be  built          | Have a clear idea of what the circuit should look like  before starting to making.                     | 20 min        | Dec 03                 | A         |
| 3       | Completing the circuit for the   sensors           | Have circuit ready to start collecting data                                                            | 30 min        | Dec 03                 | C         |
| 4       | Drawing the flow diagram for adding  a new user    | Have a clear idea of the operation and have a better understaing about how the code should be written  | 10 min        | Dec 04                 | B         |
| 5       | Adding new user to the server                      | Have an unique user for the project                                                                    | 10 min        | Dec 04                 | C         |
| 6       | Drawing the flow diagram for adding  new sensors   | Have a clear idea of the operation and have a better  understaing about how the code should be written | 15 min        | Dec 04                 | B         |
| 7       | Adding the new sensors to the server               | Having stored sensors in the server                                                                    | 20 min        | Dec 04                 | C         |
| 8       | Created the loop to upload the data  to the server | Uploading the data gotten by the sensors to the main server                                            | 10 min        | Dec 05                 | C         |
| 9       | Creating the graphs                                | Have a visual representation of the data obtained by the  sensors inside and outside the dormitory.    | 3 hrs          | Dec 13                 | C         |
| 10      | Creating the poster                                | Have a summary of introduction, materials and methods,  results, conclusions and references            | 1 hr          | Dec 13                 | D         |
| 11      | Creating the video                                 | Present how the solution works using the poster created  earlier                                       | 30 mins       | Dec 13                 | D         |
## Test Plan

# Criteria C: Development

## List of techniques used
01. Lists
02. List Comprehension
03. List slicing
04. List indexing
05. Functions
06. For/while loops
07. Range
08. Comments
09. Conditional statements
10. Dictionaries
11. Pyplot from matplotlib
12. Numpy library
13. datetime library
14. Adafruit_DHT library
15. Requests library
16. API commands
17. Data smoothing


## Development
### Code
#### Create new sensors
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

This function is designed to create four sensors in the server. First there is a for loop that will loop for four times and each time the loop is run, there will be  two temporary dictionaries created, and in the dictionaries it contains the name, the unit, the location and the type of each sensor. And after the dictionaries are  created the dictionaries are converted to JSON and then posted to http://192.168.6.142/sensor/new. And finally the function gives out the sensor id of the newly uploaded sensors' id and owner's id with details that were given when sensors were being uploaded to the server( name, unit, location and type). This function is required since we need a user in the server to post the records that we take from the sensors.

#### Get authrization key

```.py
def get_auth(user, url="http://192.168.6.142"):
    req = requests.post(f"{url}/login", json=user)
    access_token = req.json()['access_token']
    auth = {"Authorization": f"Bearer {access_token}"}
    return auth
```

Purpose of this function is to get the authorization key from the server. The username and the password are inputted as a dictionary(user) to the function. Using the request library, the username and the password is sent to the server using post. Then then the access token is taken and converted using JSON. And then the access token is stored in a dictionary called auth and the key for the token is Authorization. Finally the function returns the dictionary auth. This function is done whenever we need to get the authorization key to perform a task like posting data to the server.

#### Get data from the server

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
    
This function can be used to get the readings from the registered sensors in "http://192.168.6.142". First the id of the sensor that the data is given is inputted as id. Then the function gets data from "http://192.168.6.142/readings" and then converts the data as JSON and is stored in the variable data. The readings of sensors are stored as data_all. Then the output list is created which is empty. Then for every item in data_all the program checks if the "sensor_id" is the same as id that was inputted at the beginning of the function. And if the "sensor_id" matches with the id the readings of the sensor(which is stored in the key "value") is appended to the output list. After the loop is completed the function returns the output list. This function is used when we need to get the data of the remote server and also the data that we posted in the server.

### Test plan
| Description                             | Type           | Inputs                                                                                                                                                                                                                                                                                                                                                                                                                     | Outputs                                                                                        |
|-----------------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Representing graphs in different colors | Functional     | Remote server data                                                                                                                                                                                                                                                                                                                                                                                                         | A graph that has input in blue                                                                 |
| Labels for axis                         | Functional     | Text for each axis of the graph                                                                                                                                                                                                                                                                                                                                                                                            | A text that appears next to the graph which indicates what the axis means                      |
| The background of the graphs            | Functional     | ggplot theme                                                                                                                                                                                                                                                                                                                                                                                                               | A graph that is plotted in a gray background(The gray background is a<br>result of ggplot)     |
| User registration                       | Non-functional | user = ({"username": "Krish&Thumula", "password":"###"}).json()                                                                                                                                                                                                                                                                                                                                                            | The same dictionary is returned                                                                |
| Posting new sensors                     | Non-functional | temp_hum = ({ <br>              "name": f"Krish&Thumula Hum{i}", <br>              "unit": "%", <br>              "location": "R1-14B", <br>              "type": "Humditiy"<br>               }).json()<br>temp_temp = ({ <br>              "name": f"Krish&Thumula Temp{i}", <br>              "unit": "C", <br>              "location": "R1-14B", <br>              "type": "Temperature" <br>               }).json() | The server returns the details of the sensor registered in the server                          |
| Prediction graphs                       | Non-functional | The cubic equation for the graph                                                                                                                                                                                                                                                                                                                                                                                           | The predictedion is given by a blue crossed line which will be connected<br>to the cubic graph |

### Computational skills

#### Remote data
##### All the graphs
![remote_data](https://user-images.githubusercontent.com/50672613/207284768-683f30cb-169a-44c7-8828-7259c0e24eb0.png)

**Fig.5:** This figure shows remote data. 

For these graphs we first got the raw data from the server for humidity and temperature and plotted it using matplotlib.pyplot. Then we smoothed the data 
and created a smoothed version of the previous graph. Then we used numpy to get a non-linear equation so we would be able to extend the graph and get the 
predicted data.

##### Raw temperature
![remote_raw_temp](https://user-images.githubusercontent.com/50672613/207285460-36254f70-3c72-4f25-bd85-6a7a4b8977dd.png)

**Fig.6:** This graph shows the raw temperature data of the campus

##### Smoothed temperature data
![remote_processed_temp](https://user-images.githubusercontent.com/50672613/207285747-1361978b-fcde-4ebc-885b-cb077d760c5d.png)

**Fig.7:** This graph shows the smoothed version of the temperature data of the campus with non-linear model, 12 hour prediction, min, max, mean

Temperature model formula: -0.00000x^3 + 0.00031x^2 + -0.84613x + 732.45433

##### Raw humidity
![remote_raw_humidity](https://user-images.githubusercontent.com/50672613/207286209-94b447b7-b9a8-4843-9b5d-5238e3ee540d.png)

**Fig.8:** This graph shows the raw humidity data of the campus

##### Smoothed humidity data
![remote_processed_humidity](https://user-images.githubusercontent.com/50672613/207286266-0fc0f8f9-41e3-4d94-bbe0-0112d4d2ac9a.png)

**Fig.9:** This graph shows the smoothed version of the humidity data of the campus with non-linear model, 12 hour prediction, min, max, mean

Humidity model formula: 0.00000x^3 + -0.00256x^2 + 5.468367x + -3825.32962

#### Local data
##### Smoothed temperature data
![local_smooth_data](https://user-images.githubusercontent.com/50672613/207284509-b3509199-bd5e-4baf-b98e-b89818ee5f7d.png)
**Fig.10:** This graph shows the smoothed, raw temperature data of the room

Temperature model formula: 0.00012x^3 + -0.02097x^2 + 0.84810x + 21.23204

We obtained the above model using numpy and the used GridSpec to display the graphs like this.

##### Smoothed humidity data
![local_smooth_hum](https://user-images.githubusercontent.com/50672613/207313500-77b5cc88-730a-4441-87e6-fe21fcd57ae3.png)

Humidity model formula: -0.00003x^3 + 0.00706x^2 + -0.443113x + 26.25557

We obtained the above model using numpy and the used GridSpec to display the graphs like this.

**Fig.11:** This graph shows the smoothed raw humidity data of the campus

##### Smoothed local data with predictions
![local_data](https://user-images.githubusercontent.com/50672613/207313582-f05fb3bb-836b-4543-b7b6-69635feb7539.png)


**Fig.12:** This graph shows the smoothed version of the humidity data of the campus with non-linear model, 12 hour prediction, min, max, mean

For these graphs we first got the raw data from the server that we uploaded to the server humidity and temperature and plotted it using matplotlib.pyplot. Then we smoothed the data and created a smoothed version of the previous graph. Then we used numpy to get a non-linear equation so we would be able to extend the graph and get the predicted data.


# Criteria D: Functionality

[A 7 min video demonstrating the proposed solution with narration]() 

[The poster](https://github.com/krishank-gupta/unit2_project/blob/main/Poster_of_Krish%26Thumula.pdf)


