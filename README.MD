# weatherfetch

A neofetch-inspired CLI tool that displays current weather conditions for any location, alongside ASCII art that reflects the current weather condition.


## Requirements

- Python 3.10+
- `requests` library

Install dependencies:

```
pip install -r requirements.txt
```

## Usage

Run with no arguments to use your current location (detected via IP):

```
python3 fetch.py
```

Specify a city with the `-l` flag:

```
python3 fetch.py -l miami
python3 fetch.py -l "deerfield beach"
```

Specify a unit system with the `-u` flag:

```
python3 fetch.py -u imperial
python3 fetch.py -u metric
python3 fetch.py -u i
python3 fetch.py -u m
```

Combine flags:

```
python3 fetch.py -l chicago -u metric
```

## Configuration

Edit `config.py` to set your personal defaults:

```python
# Default unit system: "imperial" or "metric"
DEFAULT_UNIT = "imperial"

# Default city when no -l flag is provided (unused if auto location works)
DEFAULT_CITY = "miami"

# Minimum width of the ASCII art column
MIN_WIDTH = 15

# Info fields to display — comment out any line to hide it
DISPLAY_INFO = [
    "city",
    "temperature",
    "feels_like",
    "humidity",
    "wind_speed",
    "precipitation",
    "cloud_cover",
    "uv_index",
    "condition",
]

# Terminal color slots — change these to match your terminal theme
COLOR2 = "\033[32m"  # used for info label headers
```

## Supported Weather Conditions

| Condition | WMO Codes |
|-----------|-----------|
| Sunny | 0 |
| Cloudy | 1, 2, 3 |
| Rainy | 51, 53, 55, 61, 63, 65, 80, 81, 82 |
| Stormy | 17 |
| Snowy | 22, 23, 24, 26, 27, 36, 37, 38, 39, 66, 67, 68, 69 |

## APIs Used

- [Open-Meteo](https://open-meteo.com/) — weather data and geocoding (free, no API key required)
- [ip-api.com](http://ip-api.com/) — IP-based location detection (free, no API key required)

## Project Structure

```
weatherfetch/
    fetch.py          — main logic and entry point
    weather_icons.py  — ASCII art and weather condition mapping
    config.py         — user preferences and color settings
    requirements.txt  — dependencies
    README.md         — this file
```
