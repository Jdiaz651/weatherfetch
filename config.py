# config.py
from requests.models import REDIRECT_STATI

DEFAULT_UNIT = "imperial"
DEFAULT_CITY = "miami"
MIN_WIDTH = 15

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


# terminal color slots
BOLD = "\033[1m"
RESET = "\033[0m"
COLOR1 = "\033[38;5;1m"
COLOR2 = "\033[38;5;2m"
COLOR3 = "\033[38;5;3m"
COLOR4 = "\033[38;5;4m"
COLOR5 = "\033[38;5;5m"
COLOR6 = "\033[38;5;6m"
COLOR7 = "\033[38;5;7m"
