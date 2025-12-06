"""
This script uses the Weatherstack API to retrieve and display current weather 
information for a user-specified city.

The program prompts the user to enter a city name, makes an API request to 
Weatherstack, and displays  weather data.

The user can continue searching for different cities until a valid result 
is retrieved.

Author: Eric
Date: December 2025
"""

import requests

api_key = "08eadc43987b4743390c3e029686caf3"

while True:
    city = input("Enter city name to check current weather: ")
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"

    r = requests.get(url)

    if r.status_code == 200:
        result = r.json()

        if 'error' in result:
            print("Error, Please try again")
            continue
    
        location = result['location']['name']
        country = result['location']['country']
        temperature = result['current']['temperature']
        weather_desc = result['current']['weather_descriptions'][0]
        humidity = result['current']['humidity']
        wind_speed = result['current']['wind_speed']
        feels_like = result['current']['feelslike']

        print(f"Location: {location}, {country}")
        print(f"Temperature: {temperature} degrees, feels like {feels_like} degrees")
        print(f"Conditions: {weather_desc}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} km/h")

    else:
        print("Error: Request Failed!")