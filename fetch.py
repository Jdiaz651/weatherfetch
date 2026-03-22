import argparse
from itertools import zip_longest

import requests

from weather_icons import get_weather_icon, weather_icons


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", help="city name")
    args = parser.parse_args()

    if args.l:
        lat, lon = get_coordinates(args.l)
        results = get_weather(lat, lon)
        condition = get_weather_icon(results["current"]["weather_code"])
        art = weather_icons[condition].splitlines()
        art_width = max(len(line) for line in art) + 3

        info = [
            f"City: {args.l}",
            f"Temp: {results['current']['temperature_2m']}°F",
            f"Humidity: {results['current']['relative_humidity_2m']}%",
            f"Condition: {condition}",
            f"Feels Like: {results['current']['apparent_temperature']}°F",
            f"Wind: {results['current']['wind_speed_10m']} mph",
            f"Precipitation: {results['current']['precipitation']} mm",
            f"Cloud Cover: {results['current']['cloud_cover']}%",
            f"UV Index: {results['current']['uv_index']}",
        ]

        for art_line, info_line in zip_longest(art, info, fillvalue=""):
            print(f"{art_line:<{15}}  {info_line}")
