import pandas as pd
import pytest

from zc_flightplan_toolkit.api import (
    CheckWxAPI,
    ClowdIoDATISAPI,
    FlightAwareAPI,
    FlightInfoAPI,
)


@pytest.fixture
def flightaware_api() -> FlightInfoAPI:
    return FlightAwareAPI()


@pytest.mark.parametrize(
    "airport_id, country_code",
    [
        ("WSSS", "SG"),
        ("WMKK", "MY"),
        ("KIAH", "US"),
    ],
)
def test_get_airport_info(
    airport_id: str, country_code: str, flightaware_api: FlightInfoAPI
):
    api = flightaware_api
    airport_info = api.get_airport_information(airport_id)
    assert isinstance(airport_info, pd.DataFrame)
    assert airport_info["country_code"].iloc[0] == country_code


def test_get_route_info(flightaware_api: FlightInfoAPI):
    api = flightaware_api
    route_info = api.get_route_info("KLAX", "KJFK")
    assert isinstance(route_info, pd.DataFrame)
    assert "route" in route_info.columns


@pytest.mark.parametrize(
    "airport_icao",
    [
        ("KLAX"),
        ("KMIA"),
    ],
)
def test_get_datis(airport_icao: str):
    api = ClowdIoDATISAPI()
    atis = api.request_datis(airport_icao)
    assert "ATIS" in atis


@pytest.mark.parametrize(
    "icao",
    [
        ("wsss"),
        ("KLAX"),
    ],
)
def test_weather_api_raw_metar(icao):
    api = CheckWxAPI()
    metar = api.get_metar(icao)
    assert isinstance(metar, str)


@pytest.mark.parametrize(
    "icao",
    [
        ("wsss"),
        ("KLAX"),
    ],
)
def test_weather_api_decoded_metar(icao):
    api = CheckWxAPI()
    metar = api.get_metar(icao, decoded=True)
    assert isinstance(metar, pd.DataFrame)
