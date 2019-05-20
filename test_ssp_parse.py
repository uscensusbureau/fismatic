import csv
from docx import Document
import itertools
import ssp_parse

SOURCE_DOC = "Azure Security and Compliance Blueprint - FedRAMP High SSP.docx"


def test_matrix():
    ssp_parse.run(SOURCE_DOC)

    with open("matrix.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        column_headings = csv_reader.fieldnames[1:]
        assert column_headings[0:4] == [
            "AC-1: Part a",
            "AC-1: Part b",
            "AC-2: Part a",
            "AC-2: Part b",
        ]

        # check that the columns match the rows
        csv_reader = csv.reader(csv_file)
        row_headings = [row[0] for row in csv_reader]
        assert row_headings == column_headings


def test_get_controls():
    doc = Document(docx=SOURCE_DOC)
    tables = ssp_parse.get_tables(doc)

    controls = ssp_parse.get_controls(tables)

    control_ids = list(controls.keys())
    # TODO address inconsistent spacing
    assert control_ids[0:4] == ["AC-1", "AC-2", "AC-2(1)", "AC-2 (2)"]
