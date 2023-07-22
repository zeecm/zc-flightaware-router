from enum import Enum
from typing import NamedTuple, Protocol

import pandas as pd

from zc_flightplan_toolkit.utils import get_unique_value


class RunwayData(Enum):
    IDENT = "ident"
    HEADING = "heading"
    LONGITUDE = "longitude"
    LATITUDE = "latitude"
    THRESHOLD_ELEVATION = "threshold_elevation"
    DISPLACED_THRESHOLD = "displaced_threshold"


class RunwayInfo(NamedTuple):
    ident: str = "NA"
    heading: int = 0
    longitude: float = 0.0
    latitude: float = 0.0
    threshold_elevation: int = 0
    displaced_threshold: int = 0


class AirportRunwayInfo(Protocol):
    data: pd.DataFrame

    def get_airport_runways(self, icao: str) -> pd.DataFrame:
        ...

    def get_runway_info(self, icao: str, runway_ident: str) -> RunwayInfo:
        ...


class DMColumns(Enum):
    ICAO = "airport_ident"
    LENGTH = "length_ft"
    WIDTH = "width_ft"
    SURFACE = "surface"
    LIGHTED = "lighted"
    CLOSED = "closed"
    LEFT_END_IDENT = "le_ident"
    LEFT_END_LATITUDE = "le_latitude_deg"
    LEFT_END_LONGITUDE = "le_longitude_deg"
    LEFT_END_THRESHOLD_ELEVATION = "le_elevation_ft"
    LEFT_END_HEADING = "le_heading_degT"
    LEFT_END_DISPLACED_THRESHOLD = "le_displaced_threshold_ft"
    RIGHT_END_IDENT = "he_ident"
    RIGHT_END_LATITUDE = "he_latitude_deg"
    RIGHT_END_LONGITUDE = "he_longitude_deg"
    RIGHT_END_THRESHOLD_ELEVATION = "he_elevation_ft"
    RIGHT_END_HEADING = "he_heading_degT"
    RIGHT_END_DISPLACED_THRESHOLD = "he_displaced_threshold_ft"


DM_END_INFO_MAP = {
    DMColumns.LEFT_END_IDENT: {
        RunwayData.LATITUDE: DMColumns.LEFT_END_LATITUDE,
        RunwayData.LONGITUDE: DMColumns.LEFT_END_LONGITUDE,
        RunwayData.THRESHOLD_ELEVATION: DMColumns.LEFT_END_THRESHOLD_ELEVATION,
        RunwayData.HEADING: DMColumns.LEFT_END_HEADING,
        RunwayData.DISPLACED_THRESHOLD: DMColumns.LEFT_END_DISPLACED_THRESHOLD,
    },
    DMColumns.RIGHT_END_IDENT: {
        RunwayData.LATITUDE: DMColumns.RIGHT_END_LATITUDE,
        RunwayData.LONGITUDE: DMColumns.RIGHT_END_LONGITUDE,
        RunwayData.THRESHOLD_ELEVATION: DMColumns.RIGHT_END_THRESHOLD_ELEVATION,
        RunwayData.HEADING: DMColumns.RIGHT_END_HEADING,
        RunwayData.DISPLACED_THRESHOLD: DMColumns.RIGHT_END_DISPLACED_THRESHOLD,
    },
}


class DMAirportRunwayInfo:
    def __init__(
        self,
        info_source: str = "https://davidmegginson.github.io/ourairports-data/runways.csv",
    ):
        self.data = pd.read_csv(info_source)

    def get_airport_runways(self, icao: str) -> pd.DataFrame:
        airport_data = self._get_runways_info_for_airport(icao)
        left_end_idents = airport_data[DMColumns.LEFT_END_IDENT.name].unique().tolist()
        right_end_idents = (
            airport_data[DMColumns.RIGHT_END_IDENT.name].unique().tolist()
        )
        all_runway_idents = left_end_idents + right_end_idents

        rows_with_runway_info = []
        for ident in all_runway_idents:
            runway_info = self.get_runway_info(icao, ident)
            rows_with_runway_info.append(runway_info._asdict())
        return pd.DataFrame(rows_with_runway_info)

    def get_runway_info(self, icao: str, runway_ident: str) -> RunwayInfo:
        runway_ident = runway_ident.upper()

        runway_info = self._get_runway_info_matching_ident(icao, runway_ident)

        runway_end_enum = self._find_end_that_matches_ident(runway_info, runway_ident)

        return self._generate_runway_info(runway_info, runway_end_enum)

    def _get_runway_info_matching_ident(
        self, icao: str, runway_ident: str
    ) -> pd.DataFrame:
        airport_data = self._get_runways_info_for_airport(icao)

        left_end_match = airport_data[DMColumns.LEFT_END_IDENT.name] == runway_ident
        right_end_match = airport_data[DMColumns.RIGHT_END_IDENT.name] == runway_ident

        return airport_data[(left_end_match | right_end_match)]

    def _get_runways_info_for_airport(self, icao: str) -> pd.DataFrame:
        airport_data = self.data[self.data[DMColumns.ICAO.value] == icao.upper()]
        rename_map = {col.value: col.name for col in DMColumns}
        airport_data = airport_data.rename(columns=rename_map, errors="raise")
        final_colmnns = [col.name for col in DMColumns]
        return airport_data[final_colmnns]

    def _find_end_that_matches_ident(
        self, runway_info: pd.DataFrame, runway_ident: str
    ) -> DMColumns:
        ident_match = runway_info.eq(runway_ident)
        column_with_ident = ident_match.any(axis=0)
        column_name = runway_info.columns[column_with_ident].to_list()[0]
        return DMColumns[column_name]

    def _generate_runway_info(
        self, runway_info: pd.DataFrame, runway_end_enum: DMColumns
    ) -> RunwayInfo:
        ident_col = runway_end_enum.name

        runway_end_info_columns = DM_END_INFO_MAP[runway_end_enum]

        longitude_col = runway_end_info_columns[RunwayData.LONGITUDE].name
        latitude_col = runway_end_info_columns[RunwayData.LATITUDE].name
        heading_col = runway_end_info_columns[RunwayData.HEADING].name
        threshold_elevation_col = runway_end_info_columns[
            RunwayData.THRESHOLD_ELEVATION
        ].name
        displaced_threshold_col = runway_end_info_columns[
            RunwayData.DISPLACED_THRESHOLD
        ].name

        ident = get_unique_value(runway_info, ident_col, str)
        longitude = get_unique_value(runway_info, longitude_col, float)
        latitude = get_unique_value(runway_info, latitude_col, float)
        heading = get_unique_value(runway_info, heading_col, int)
        threshold_elevation = get_unique_value(
            runway_info, threshold_elevation_col, int
        )
        displaced_threshold = get_unique_value(
            runway_info, displaced_threshold_col, int
        )

        return RunwayInfo(
            ident=ident,
            heading=heading,
            longitude=longitude,
            latitude=latitude,
            threshold_elevation=threshold_elevation,
            displaced_threshold=displaced_threshold,
        )
