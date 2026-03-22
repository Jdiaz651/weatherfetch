import argparse
import sys
from itertools import zip_longest

import requests
from requests.sessions import Request

from weather_icons import weather_icons

parser = argparse.ArgumentParser()
parser.add_argument("-l", help="city name")
args = parser.parse_args()


# grabs data from open meteo and prints the latitude and longitude of a location
def get_coordinates(city):
    api_requests = {"name": city}
    data = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search", params=api_requests
    ).json()
    lat = data["results"][0]["latitude"]
    lon = data["results"][0]["longitude"]

    return (lat, lon)


def get_weather(lat, lon):
    api_requests = {
        "latitude": lat,
        "longitude": lon,
        "current": "weather_code,temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m,precipitation,cloud_cover,uv_index",
        "temperature_unit": "fahrenheit",
    }
    data = requests.get(
        "https://api.open-meteo.com/v1/forecast", params=api_requests
    ).json()
    return data


if args.l:
    lat, lon = get_coordinates(args.l)
    results = get_weather(lat, lon)

    art = weather_icons["sunny"].splitlines()
    lines = art.count("\n")
    art_width = max(len(line) for line in art) + 3

    info = [
        f"City: {args.l}",
        f"Temp: {results['current']['temperature_2m']}°F",
        f"Humidity: {results['current']['relative_humidity_2m']}%",
    ]

    for art_line, info_line in zip_longest(art, info, fillvalue=""):
        print(f"{art_line:<{art_width}}  {info_line}")
