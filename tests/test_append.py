import polars as pl
import polarsbear as pb
import numpy as np


def test_concat() -> None:
    df1 = pl.DataFrame({"a": [1], "b": [2], "c": [3]})
    df2 = pl.DataFrame({"a": [4], "b": [5], "c": [6]})

    df3 = pb.concat([df1, df2])

    assert df3.row(0) == df1.row(0)
    assert df3.row(1) == df2.row(0)
