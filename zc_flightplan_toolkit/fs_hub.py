import json
from typing import Any, Dict, Union

import pandas as pd

from zc_flightplan_toolkit.api import BaseAPI
from zc_flightplan_toolkit.constants import FS_HUB_API_KEY, FS_HUB_API_URL
from zc_flightplan_toolkit.utils import format_utc_time, get_time_diff_minutes


class FsHubAPI(BaseAPI):
    def __init__(self, api_url: str = FS_HUB_API_URL, api_key: str = FS_HUB_API_KEY):
        self._api_url = api_url
        self._request_header = {"X-Pilot-Token": api_key}

    def get_pilot_flights(
        self, pilot_id: int, page_size: int = 100, pages_to_get: int = 10
    ) -> list[Dict[str, Any]]:
        cursor = 0
        current_page = 0

        pilot_flights: list[Dict[str, Any]] = []

        while current_page <= pages_to_get:
            pilot_flights_endpoint = (
                f"pilot/{pilot_id}/flight?limit={page_size}&cursor={cursor}"
            )
            response = self._make_api_call(pilot_flights_endpoint)
            response_dict: Dict[str, Any] = json.loads(response.text)

            if ("meta" not in response_dict) or ("data" not in response_dict):
                raise KeyError(f"invalid response: {response.text}")

            count = response_dict["meta"]["cursor"]["count"]

            if count < page_size:
                break

            cursor = response_dict["meta"]["cursor"]["next"]
            current_page += 1

            pilot_flights_data = response_dict["data"]
            pilot_flights.extend(pilot_flights_data)

        return pilot_flights


def get_pilot_flights_in_volanta_format():
    fs_hub_api = FsHubAPI()
    pilot_flights = fs_hub_api.get_pilot_flights(pilot_id=3506)

    formatted_pilot_flights: list[Dict[str, Union[str, int]]] = []

    for flight in pilot_flights:
        departure = flight["departure"]
        arrival = flight["arrival"]
        distance = flight["distance"] or {"nm": 0}
        if not departure or not arrival:
            continue

        duration = get_time_diff_minutes(start=departure["time"], end=arrival["time"])

        if duration <= 10:
            continue

        flight_data = {
            "AircraftType": flight["aircraft"]["icao"],
            "Origin": departure["icao"],
            "Destination": arrival["icao"],
            "DepartureTime": format_utc_time(departure["time"]),
            "ArrivalTime": format_utc_time(arrival["time"]),
            "Distance": distance["nm"],
            "Fuel": departure["fuel"] - arrival["fuel"],
            "Duration": duration,
        }

        formatted_pilot_flights.append(flight_data)

    pilot_flights_df = pd.DataFrame(formatted_pilot_flights)
    pilot_flights_df.to_csv("zc_flights.csv", index=False)
