from docx import Document
from . import common
from .. import parser


def test_get_controls():
    doc = Document(docx=common.SOURCE_DOC)
    tables = parser.get_tables(doc)

    controls = parser.get_controls(tables)

    control_ids = list(controls.keys())
    # TODO address inconsistent spacing
    assert control_ids[0:4] == ["AC-1", "AC-2", "AC-2(1)", "AC-2 (2)"]
