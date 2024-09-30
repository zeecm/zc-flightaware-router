import os
from enum import Enum

from dotenv import load_dotenv

load_dotenv()

FLIGHTAWARE_API_ENV = os.environ.get("FLIGHTAWARE_API_ENV", "aeroapi")

FLIGHTAWARE_API_URL = f"https://{FLIGHTAWARE_API_ENV}.flightaware.com/aeroapi"

DATIS_ENDPOINT = "http://datis.clowd.io/api/"

AERO_API_KEY = os.environ.get("AERO_API_KEY", "")

FS_HUB_API_KEY = os.environ.get("FS_HUB_API_KEY", "")

FS_HUB_API_URL = "https://fshub.io/api/v3"

CHECKWX_API_KEY = os.environ.get("CHECKWX_API_KEY", "")

CHECKWX_API_URL = "https://api.checkwx.com"


class FlightAwareAirportColumns(Enum):
    ICAO = "code_icao"
    IATA = "code_iata"
    LID = "code_lid"
    NAME = "name"
    ELEVATION = "elevation"
    CITY = "city"
    STATE = "state"
    LONGITUDE = "longitude"
    LATITUDE = "latitude"
    TIMEZONE = "timezone"
    COUNTRY_CODE = "country_code"
    WIKI_URL = "wiki_url"
    FLIGHTS_API_ENDPOINT = "airport_flights_url"


class DATISInfo(Enum):
    AIRPORT = "airport"
    TYPE = "type"
    CODE = "code"
    ATIS = "datis"


class Preferences(Enum):
    AERO_API_KEY = "aero_api_key"
    CHECKWX_API_KEY = "checkwx_api_key"
