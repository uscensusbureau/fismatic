from . import common
from ..docx_parser import DocxParser


def test_get_controls():
    parser = DocxParser(common.SOURCE_DOC)

    controls = parser.get_controls()

    control_ids = list(controls.keys())
    # TODO address inconsistent spacing
    assert control_ids[0:4] == ["AC-1", "AC-2", "AC-2(1)", "AC-2 (2)"]
