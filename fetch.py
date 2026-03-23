import argparse
from itertools import zip_longest

import requests

from config import DEFAULT_UNIT, DISPLAY_INFO, MIN_WIDTH
from weather_icons import get_weather_icon, weather_icons


# returns lat and lon for a given city name
def get_coordinates(city):
    api_requests = {"name": city}
    data = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search", params=api_requests
    ).json()
    lat = data["results"][0]["latitude"]
    lon = data["results"][0]["longitude"]
    return (lat, lon)


def get_current_coordinates():
    results = requests.get("http://ip-api.com/json/").json()
    lat = results["lat"]
    lon = results["lon"]
    city = results["city"]
    return (lat, lon, city)


def get_weather(lat, lon, unit):
    api_requests = {
        "latitude": lat,
        "longitude": lon,
        "current": "weather_code,temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m,precipitation,cloud_cover,uv_index",
        "temperature_unit": "fahrenheit" if unit == "imperial" else "celsius",
        "wind_speed_unit": "mph" if unit == "imperial" else "kmh",
        "precipitation_unit": "inch" if unit == "imperial" else "mm",
    }
    data = requests.get(
        "https://api.open-meteo.com/v1/forecast", params=api_requests
    ).json()
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", help="city name")
    parser.add_argument("-u", help="unit system", default=DEFAULT_UNIT)
    args = parser.parse_args()

    if args.u == ("imperial" or "i"):
        units = "imperial"
        temp_label = "°F"
        wind_label = "mph"
        precip_label = "in"
    else:
        units = "metric"
        temp_label = "°C"
        wind_label = "km/h"
        precip_label = "mm"

    if args.l:
        lat, lon = get_coordinates(args.l)
        city = args.l
    else:
        lat, lon, city = get_current_coordinates()

    results = get_weather(lat, lon, units)
    condition = get_weather_icon(results["current"]["weather_code"])
    art = weather_icons[condition].splitlines()
    art_width = max(len(line) for line in art) + 3
    max(art_width, MIN_WIDTH)

    info_options = {
        "city": f"City: {city}",
        "temperature": f"Temp: {results['current']['temperature_2m']}{temp_label}",
        "feels_like": f"Feels Like: {results['current']['apparent_temperature']}{temp_label}",
        "humidity": f"Humidity: {results['current']['relative_humidity_2m']}%",
        "wind_speed": f"Wind: {results['current']['wind_speed_10m']} {wind_label}",
        "precipitation": f"Precipitation: {results['current']['precipitation']} {precip_label}",
        "cloud_cover": f"Cloud Cover: {results['current']['cloud_cover']}%",
        "uv_index": f"UV Index: {results['current']['uv_index']}",
        "condition": f"Condition: {condition}",
    }
    info = [info_options[key] for key in DISPLAY_INFO if key in info_options]

    for art_line, info_line in zip_longest(art, info, fillvalue=""):
        print(f"{art_line:<{art_width}}  {info_line}")
