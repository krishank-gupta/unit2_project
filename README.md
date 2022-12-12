![weather.png](weather_asbt.png)

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

![](https://github.com/krishank-gupta/unit2_project/blob/main/sysdim_hl.png.png)

**Fig.1** shows the system diagram for the proposed solution (**HL**). The indoor variables will be measured using a Raspberry PI and four DHT11 sensors located inside a room. Four sensors are used to determine more precisely the physical values and include measurement uncertainty. The outdoor variables will be requested to the remote server using a GET request to the API of the server at ```192.168.6.147/readings```. The local values are stored in a CSV database locally and POST to the server using the API and TOKEN authentication. A laptop computer is used for remotely controlling the local Rasberry Pi using a Dekptop sharing application (VNC Viewer). (Optional) Data from the local raspberry is downloaded to the laptop for analysis and processing.


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
| 10      | Creating the poster                                | Have a summary of introduction, materials and methods,  results, conclusions and references            | 1 hr          | Dec 13                 | C         |
| 11      | Creating the video                                 | Present how the solution works using the poster created  earlier                                       | 30 mins       | Dec 13                 | C         |
## Test Plan

# Criteria C: Development

## List of techniques used
1. Lists
2. Functions
3. For/while loops
4. If,elif,else statements
5. List Comprehension(Not sure if we used this but I kind of think)
6. Dictionaries
7. Pyplot from matplotlib
8. Numpy

## Development


# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration 

