import csv
import os.path
import pandas as pd
import pytest
from . import common
from .. import core as fismatic


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (common.SOURCE_DOC, [common.SOURCE_DOC]),  # single file
        (".", [common.SOURCE_DOC]),  # directory with docx
        ("out", []),  # directory without docx
    ],
)
def test_get_files(test_input, expected):
    result = fismatic.get_files(test_input)

    # absolute-ize the paths so that it doesn't fail due to leading `./`s
    result = [os.path.abspath(p) for p in result]
    expected = [os.path.abspath(p) for p in expected]

    assert result == expected


def test_matrix():
    fismatic.run(common.SOURCE_DOC)

    df = pd.read_csv(
        "out/Azure Security and Compliance Blueprint - FedRAMP High SSP.csv",
        index_col=0,
    )
    column_names = df.columns
    assert list(column_names[0:4]) == [
        "AC-1: Part a",
        "AC-1: Part b",
        "AC-2: Part a",
        "AC-2: Part b",
    ]
    # check that the columns match the rows
    row_names = df.index
    assert list(column_names) == list(row_names)
