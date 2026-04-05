# TO BE FIXED

from urllib import response

import requests
import sys
from dotenv import load_dotenv
import os

# API key aus .env laden
load_dotenv()
API_KEY = os.getenv('API_KEY')

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "en"
    }
    response = requests.get(BASE_URL, params=params)

    print(response.status_code)
    print(response.json())

    if response.status_code == 404:
        print(f"Stadt '{city}' nicht gefunden.")
        return
    if response.status_code != 200:
        print(f"Fehler: {response.status_code}")
        return

    data = response.json()
    city_name = data["name"]
    temp = data["main"]["temp"]
    # usw.

    print(f"In {city_name} there are {temp} degrees Celsius")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Verwendung: python weather.py <Stadt>")
        sys.exit(1)


    get_weather("Vienna")

