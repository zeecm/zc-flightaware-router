import os
from enum import Enum

FLIGHTAWARE_API_ENV = os.environ.get("FLIGHTAWARE_API_ENV", "aeroapi")

FLIGHTAWARE_API_URL = f"https://{FLIGHTAWARE_API_ENV}.flightaware.com/aeroapi"

AEROAPI_KEY = os.environ.get("AEROAPI_KEY", "LZ2dw1SZrAA9eGjsU8sv2PdrmMBedOp3")

DATIS_ENDPOINT = "http://datis.clowd.io/api/"


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
