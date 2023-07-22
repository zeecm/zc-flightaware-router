from typing import Type, TypeVar

import pandas as pd
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
