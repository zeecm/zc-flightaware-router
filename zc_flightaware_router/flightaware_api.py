import json
import os
from typing import Any, Dict, List, Literal, Optional

import pandas as pd
import requests
from dotenv import load_dotenv
from loguru import logger
from requests import Response

load_dotenv()

FLIGHTAWARE_API_ENV = os.environ.get("FLIGHTAWARE_API_ENV", "aeroapi")

FLIGHTAWARE_API_URL = f"https://{FLIGHTAWARE_API_ENV}.flightaware.com/aeroapi"

AEROAPI_KEY = os.environ.get("AEROAPI_KEY", "LZ2dw1SZrAA9eGjsU8sv2PdrmMBedOp3")


class FlightAwareAPI:
    """Class to interface with Flight Aware's API to retrieve information"""

    def __init__(self, api_url: str = FLIGHTAWARE_API_URL, api_key: str = AEROAPI_KEY):
        self._api_url = api_url
        self._request_header = {"x-apikey": api_key}

    def _make_api_call(
        self,
        api_endpoint: str,
        params: Optional[Dict[str, str | int]] = None,
        timeout: int = 5,
    ) -> Response:
        params = params or {}
        response = requests.get(
            f"{self._api_url}/{api_endpoint}",
            params=params,
            headers=self._request_header,
            timeout=timeout,
        )
        if response.status_code != 200:
            error = response.text
            logger.warning(f"Did not manage to make a successful connection: {error}")
        return response

    def get_airport_information(self, airport_id: str) -> pd.DataFrame:
        """Accepts airport ID in the form of ICAO or LID airport code

        Data returned includes airport name, city, state (when known), latitude, longitude, and timezone.
        """

        airport_info_endpoint = f"airports/{airport_id}"
        response = self._make_api_call(airport_info_endpoint)

        full_airport_info: Dict[str, Any] = json.loads(response.text)
        try:
            final_airport_info = self._process_airport_info(full_airport_info)
        except KeyError:
            final_airport_info = [full_airport_info]

        return pd.DataFrame(final_airport_info)

    def _process_airport_info(
        self, airport_info: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        best_match_info = {
            key: value for key, value in airport_info.items() if key != "alternatives"
        }
        alternative_airport_info: List[Dict[str, Any]] = airport_info["alternatives"]
        return [best_match_info] + alternative_airport_info

    def get_route_info(
        self,
        start_airport: str,
        end_airport: str,
        sort_by: Literal["count", "last_departure_time"] = "count",
        max_route_age_days: int = 6,
        max_pages: int = 1,
    ) -> pd.DataFrame:
        """Accepts airport ID in the form of ICAO or LID airport code

        Returns information about assigned IFR routings between two airports."""

        params = {
            "sort_by": sort_by,
            "max_file_age": f"{max_route_age_days} days",
            "max_pages": max_pages,
        }

        route_info_endpoint = f"airports/{start_airport}/routes/{end_airport}"
        response = self._make_api_call(route_info_endpoint, params)

        route_info_df = pd.DataFrame(json.loads(response.text)["routes"])

        return self._process_route_info(route_info_df)

    def _process_route_info(self, route_info: pd.DataFrame) -> pd.DataFrame:
        try:
            route_info["aircraft_types"] = route_info["aircraft_types"].apply(
                lambda aircrafts: ", ".join(set(aircrafts))
            )
            route_info["filed_altitude_max"] = "FL" + route_info[
                "filed_altitude_max"
            ].astype(str)
            route_info["filed_altitude_min"] = "FL" + route_info[
                "filed_altitude_min"
            ].astype(str)
            route_info["last_departure_time"] = pd.to_datetime(
                route_info["last_departure_time"]
            ).dt.strftime("%Y-%m-%d %H:%M:%S")
        except KeyError:
            route_info = pd.DataFrame({"error": "invalid or missing data"}, index=[0])
        return route_info


if __name__ == "__main__":
    api = FlightAwareAPI()
    route_info = api.get_route_info("KLAX", "KJFK")
    print("pass")
