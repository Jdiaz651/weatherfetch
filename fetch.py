import argparse

import requests
from requests.sessions import Request

from weather_icons import weather_icons

parser = argparse.ArgumentParser()
parser.add_argument("-l", help="city name")
args = parser.parse_args()


# grabs all data
def get_coordinates(city):
    api_requests = {"name": city}
    data = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search", params=api_requests
    ).json()
    lat = data["results"][0]["latitude"]
    lon = data["results"][0]["longitude"]

    print(lat, lon)


get_coordinates(args.l)
