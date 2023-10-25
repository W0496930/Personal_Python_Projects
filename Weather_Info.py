#Import request and pprint modules.
import requests
from pprint import pprint

#Use the API key given by openweathermap.org to establish the API_Key variable.
API_Key = "bf4c9906c870ca072421a37ad88a25d8"

#Establish the city string and prompt the user to enter a city.
city:str
city = input("Enter a city: ")

#Establish the URL that the program will send the user input to.
base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" +API_Key+"&q="+city

#Grab the weather data of the city that the user chose.
weather_data = requests.get(base_url).json()

#Print the weather data.
pprint(weather_data)

