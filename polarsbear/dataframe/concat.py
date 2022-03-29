import polars as pl

from polarsbear.dataframe.dataframe import DataFrame

from typing import List


def concat(dataframes: List[DataFrame]) -> DataFrame:
    """Concatentate multiple dataframes with isolated memory.

    Args:
        dataframes (List[DataFrame]): List of DataFrames to concatenate.

    Returns:
        DataFrame: Appended DataFrames.
    """
    if not dataframes:
        raise Exception("No dataframes were given.")

    res = dataframes[0]
    for df in dataframes[1:]:
        res.extend(df)

    return res
