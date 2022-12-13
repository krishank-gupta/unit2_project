
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
