import argparse

from weather_icons import weather_icons

parser = argparse.ArgumentParser()
parser.add_argument("-l", help="city name")
args = parser.parse_args()

print(weather_icons["sunny"])
