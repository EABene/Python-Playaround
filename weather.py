import os
import requests


def weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    params = {
        "q": city,
        "appid": os.environ["OPENWEATHERMAP_KEY"],
        "units": "metric",
        "lang": "en",
        "APPID": os.environ["OPENWEATHERMAP_KEY"]
    }

    response = requests.get(url, params=params)
    data = response.json()

