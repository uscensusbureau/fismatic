import csv
import os.path
import pandas as pd
from . import common
from .. import core as fismatic


def test_glob_input():
    fismatic.run("*.docx")
    outfile = "out/Azure Security and Compliance Blueprint - FedRAMP High SSP.csv"
    assert os.path.exists(outfile)


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
