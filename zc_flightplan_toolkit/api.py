from __future__ import annotations

import json
from abc import ABC
from functools import cache
from typing import Any, Dict, List, Literal, Optional, Protocol, Union, overload

import pandas as pd
import requests
from frozendict import frozendict
from loguru import logger
from requests import Response

from zc_flightplan_toolkit.constants import (
    AERO_API_KEY,
    CHECKWX_API_KEY,
    CHECKWX_API_URL,
    DATIS_ENDPOINT,
    FLIGHTAWARE_API_URL,
    DATISInfo,
    FlightAwareAirportColumns,
)
from zc_flightplan_toolkit.runways import (
    AirportRunwayInfo,
    DMAirportRunwayInfo,
    RunwayInfo,
)
from zc_flightplan_toolkit.utils import get_unique_value


class BaseAPI(ABC):
    _api_url: str
    _request_header: Dict[str, str]

    def _make_api_call(
        self,
        api_endpoint: str,
        params: Optional[Dict[str, str | int]] = None,
        timeout: int = 5,
        cache: bool = True,
    ) -> Response:
        params = params or {}

        if cache:
            frozen_params = frozendict(params)
            return self._cached_api_call(api_endpoint, frozen_params, timeout)

        logger.info(
            f"making 1 api call to {self._api_url}/{api_endpoint} with params: {params}"
        )
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

    @cache
    def _cached_api_call(
        self,
        api_endpoint: str,
        frozen_params: Optional[frozendict[str, str | int]] = None,
        timeout: int = 5,
    ) -> Response:
        frozen_params = frozen_params or frozendict()
        params = dict(frozen_params)
        return self._make_api_call(api_endpoint, params, timeout, cache=False)


class WeatherAPI(Protocol):
    @overload
    def get_metar(self, icao: str, decoded: bool) -> pd.DataFrame:
        ...

    @overload
    def get_metar(self, icao: str) -> str:
        ...

    def get_metar(self, icao: str, **kwargs) -> Union[str, pd.DataFrame]:
        ...

    def get_taf(self, icao: str) -> str:
        ...


class CheckWxAPI(BaseAPI):
    def __init__(self, api_url: str = CHECKWX_API_URL, api_key: str = ""):
        if not api_key:
            api_key = CHECKWX_API_KEY
        self._request_header = {"X-API-Key": api_key}
        self._api_url = api_url

        self._retrieved_icao: str = ""
        self._decoded_metar: Dict[str, Any] = {}

    def get_metar(self, icao: str, **kwargs) -> Union[str, pd.DataFrame]:
        if kwargs.get("decoded", False):
            return self._get_decoded_metar(icao)

        if not self._decoded_metar and icao == self._retrieved_icao:
            return self._decoded_metar["raw_text"]

        api_endpoint = f"metar/{icao}/decoded"
        response = self._make_api_call(api_endpoint, cache=False)
        response_dict = json.loads(response.text)

        if "data" in response_dict:
            self._decoded_metar = response_dict["data"][0]
            return self._decoded_metar["raw_text"]
        return "no metar found"

    def _get_decoded_metar(self, icao: str) -> pd.DataFrame:
        if not self._decoded_metar or icao != self._retrieved_icao:
            self.get_metar(icao)
        exploded_decoded = {}
        for data, decoded_value in self._decoded_metar.items():
            if data in ["station"]:
                continue
            if isinstance(decoded_value, dict):
                exploded_decoded |= {
                    f"{data}_{nested_key}": nested_val
                    for nested_key, nested_val in decoded_value.items()
                }
            if data == "clouds":
                for idx, cloud_layer in enumerate(decoded_value):
                    for cloud_info, info_value in cloud_layer.items():
                        exploded_decoded |= {f"clouds_{idx}_{cloud_info}": info_value}
        return pd.DataFrame(exploded_decoded, index=[0]).T

    def get_taf(self, icao: str) -> str:
        raise NotImplementedError


class DATISAPI(Protocol):
    def request_datis(self, airport_icao: str, **kwargs) -> str:
        ...


class ClowdIoDATISAPI:
    def __init__(self, api_endpoint: str = DATIS_ENDPOINT):
        self._api_endpoint = api_endpoint

    def request_datis(self, airport_icao: str, timeout: int = 5, **kwargs) -> str:
        if len(airport_icao) != 4:
            raise ValueError(f"invalid icao {airport_icao}")
        response = requests.get(f"{self._api_endpoint}{airport_icao}", timeout=timeout)
        if DATISInfo.ATIS.value in response.text:
            return self._process_datis(response.text)
        error_msg = (
            f"failed to retrieve datis for {airport_icao} with error: {response.text}"
        )
        logger.warning(error_msg)
        return error_msg

    def _process_datis(self, datis_text: str) -> str:
        datis_list = eval(datis_text)

        final_atis = []

        for datis_info in datis_list:
            airport = datis_info[DATISInfo.AIRPORT.value]
            atis_type = datis_info[DATISInfo.TYPE.value]
            atis_code = datis_info[DATISInfo.CODE.value]
            atis = datis_info[DATISInfo.ATIS.value]

            final_atis.append(
                f"Airport: {airport} \nATIS Type: {atis_type} \nATIS Code: {atis_code} \nATIS: {atis} \n"
            )

        return "\n".join(final_atis)


class FlightInfoAPI(Protocol):
    def get_route_info(
        self, start_airport: str, end_airport: str, **kwargs
    ) -> pd.DataFrame:
        ...

    def get_airport_information(self, airport_id: str) -> pd.DataFrame:
        ...

    def get_datis(self) -> str:
        ...

    def get_airport_runways(self) -> pd.DataFrame:
        ...

    def get_runway_info(self, runway_ident: str) -> RunwayInfo:
        ...

    @overload
    def get_metar(self) -> str:
        ...

    @overload
    def get_metar(self, decoded: bool) -> pd.DataFrame:
        ...

    def get_metar(self, **kwargs) -> Union[str, pd.DataFrame]:
        ...

    @classmethod
    def reinitialize(cls, **kwargs) -> FlightInfoAPI:
        ...


class FlightAwareAPI(BaseAPI):
    """Class to interface with Flight Aware's API to retrieve information

    Contains code that interfaces with another API to fetch DATIS"""

    def __init__(
        self,
        api_url: str = FLIGHTAWARE_API_URL,
        api_key: str = "",
        datis_api: DATISAPI = ClowdIoDATISAPI(),
        runway_info_source: AirportRunwayInfo = DMAirportRunwayInfo(),
        weather_api: WeatherAPI = CheckWxAPI(),
    ):
        self._api_url = api_url
        self._datis_api = datis_api
        self._weather_api = weather_api
        self._runway_info_source = runway_info_source

        if not api_key:
            api_key = AERO_API_KEY

        self._request_header = {"x-apikey": api_key}

        self.current_airport_icao: Optional[str] = None

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

        airport_info = pd.DataFrame(final_airport_info)

        self.current_airport_icao = get_unique_value(
            airport_info, FlightAwareAirportColumns.ICAO.value, str
        )
        return airport_info

    def get_route_info(
        self,
        start_airport: str,
        end_airport: str,
        sort_by: Literal["count", "last_departure_time"] = "count",
        max_route_age_days: int = 6,
        max_pages: int = 1,
        **kwargs,
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

    def get_datis(self) -> str:  # sourcery skip: class-extract-method
        if self.current_airport_icao is not None:
            return self._datis_api.request_datis(self.current_airport_icao)
        error_msg = "invalid or missing airport data, no datis"
        logger.warning(error_msg)
        return error_msg

    def get_airport_runways(self) -> pd.DataFrame:
        if self.current_airport_icao is not None:
            return self._runway_info_source.get_airport_runways(
                self.current_airport_icao
            )
        error_msg = "invalid or missing airport data, unable to fetch runway info"
        logger.warning(error_msg)
        return pd.DataFrame([{"error": error_msg}])

    def get_runway_info(self, runway_ident: str) -> RunwayInfo:
        if self.current_airport_icao is not None:
            return self._runway_info_source.get_runway_info(
                self.current_airport_icao, runway_ident
            )
        error_msg = "invalid or missing airport data, unable to fetch runway info"
        logger.warning(error_msg)
        return RunwayInfo()

    def get_metar(self, **kwargs) -> Union[str, pd.DataFrame]:
        if self.current_airport_icao is not None:
            if kwargs.get("decoded", False):
                return self._weather_api.get_metar(
                    self.current_airport_icao, decoded=True
                )
            else:
                return self._weather_api.get_metar(self.current_airport_icao)
        error_msg = "invalid or missing airport data, unable to fetch metar"
        logger.warning(error_msg)
        return error_msg

    def _process_airport_info(
        self, airport_info: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        best_match_info = {
            key: value for key, value in airport_info.items() if key != "alternatives"
        }
        alternative_airport_info: List[Dict[str, Any]] = airport_info["alternatives"]
        return [best_match_info] + alternative_airport_info

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

    @classmethod
    def reinitialize(
        cls,
        api_url: str = FLIGHTAWARE_API_URL,
        api_key: str = "",
        datis_api: DATISAPI = ClowdIoDATISAPI(),
        runway_info_source: AirportRunwayInfo = DMAirportRunwayInfo(),
        weather_api: WeatherAPI = CheckWxAPI(),
        **kwargs,
    ) -> FlightInfoAPI:
        logger.info(
            f"api reinitialized with api_url: {api_url}, api_key: {api_key}, datis_api: {datis_api}, runway_info_source: {runway_info_source}, weather_api: {weather_api}"
        )
        return cls(
            api_url, api_key, datis_api, runway_info_source, weather_api, **kwargs
        )
