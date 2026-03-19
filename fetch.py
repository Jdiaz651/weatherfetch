import argparse

import requests
from requests.sessions import Request

from weather_icons import weather_icons

parser = argparse.ArgumentParser()
parser.add_argument("-l", help="city name")
args = parser.parse_args()


def get_coordinates(city):
    api_requests = {"name": city}
    data = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search", params=api_requests
    )
    return data.json()


result = get_coordinates(args.l)
print(result["results"][0]["latitude"])
print(result["results"][0]["longitude"])
