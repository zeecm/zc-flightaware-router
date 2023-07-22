import pandas as pd
import pytest

from zc_flightplan_toolkit.airport_info import DMAirportRunwayInfo


@pytest.mark.parametrize(
    "icao",
    [
        ("WSSS"),
        ("kjfk"),
        ("egLL"),
    ],
)
def test_get_airport_runway_info(icao: str):
    info = DMAirportRunwayInfo()
    airport_info = info._get_runways_info_for_airport(icao)
    assert isinstance(airport_info, pd.DataFrame)


@pytest.mark.parametrize("icao, runway", [("WSSS", "02l"), ("wsss", "02C")])
def test_get_runway_info(icao: str, runway: str):
    info = DMAirportRunwayInfo()
    runway_info = info.get_runway_info(icao, runway)
    assert isinstance(runway_info.displaced_threshold, int)
