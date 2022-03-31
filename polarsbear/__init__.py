import polars as pl

from polarsbear.concat import concat
from polarsbear.csv.csv import read_csv
from polarsbear.dataframe.dataframe import DataFrame

__version__ = "0.0.1"

__all__ = ["DataFrame", "read_csv", "concat", "pl"]
