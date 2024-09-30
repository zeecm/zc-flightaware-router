from datetime import datetime
from typing import Type, TypeVar

import pandas as pd
import pytz
from loguru import logger

RestrictedReturnType = TypeVar("RestrictedReturnType", str, int, float)


def get_unique_value(
    df: pd.DataFrame, col: str, dtype: Type[RestrictedReturnType]
) -> RestrictedReturnType:
    unique_values = df[col].fillna(dtype()).unique().tolist()
    if len(unique_values) > 1:
        logger.warning("more than 1 unique values detected, returning only first")
    elif len(unique_values) != 1:
        logger.warning("no values, returning empty string")
    return dtype(unique_values[0]) if unique_values else dtype()


def format_utc_time(timestamp: str) -> str:
    if not timestamp:
        return timestamp

    # Parse the timestamp into a datetime object
    dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")

    # Set the timezone to UTC
    dt_utc = dt.replace(tzinfo=pytz.utc)

    return dt_utc.strftime("%Y-%m-%d %H:%M")


def get_time_diff_minutes(start: str, end: str) -> int:
    # Parse the timestamps into datetime objects
    start_datetime = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S.%fZ")
    end_datetime = datetime.strptime(end, "%Y-%m-%dT%H:%M:%S.%fZ")

    # Calculate the duration
    duration = end_datetime - start_datetime

    # Get the duration in minutes
    duration_minutes = duration.total_seconds() / 60

    return int(duration_minutes)
