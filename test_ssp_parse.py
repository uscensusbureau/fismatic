import csv
import itertools
import ssp_parse


def test_matrix():
    source_doc = "Azure Security and Compliance Blueprint - FedRAMP High SSP.docx"
    ssp_parse.run(source_doc)

    # check that the columns match the rows
    with open("matrix.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        expected = ["AC-1: Part a", "AC-1: Part b", "AC-2: Part a", "AC-2: Part b"]

        column_headings = csv_reader.fieldnames[1:5]
        assert column_headings == expected

        csv_reader = csv.reader(csv_file)
        top_rows = itertools.islice(csv_reader, 4)
        row_headings = [row[0] for row in top_rows]
        assert row_headings == expected
