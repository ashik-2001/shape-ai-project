import requests
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")



file = open('weather.txt','w')
file.write("\n-------------------------------------------------------------")
file.write("\nWeather Stats for - {}  || {}".format(location.upper(), date_time))
file.write("\n-------------------------------------------------------------")
file.write("\nCurrent temperature is: {:.2f} deg C".format(temp_city))
file.write("\nCurrent weather desc  :" + weather_desc+ "\n")
humidity = str(hmdt)
file.write("Current Humidity"+humidity+"")
speed = str(wind_spd)
file.write("Current wind speed    :"+speed+"kmph")
with open("weather.txt") as file:  
    data = file.read()
print(data)



file.close()
