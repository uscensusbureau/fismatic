from . import common
from ..docx_parser import DocxParser


def test_get_controls():
    parser = DocxParser(common.SOURCE_DOC)

    controls = parser.get_controls()

    control_ids = list(controls.keys())
    # TODO address inconsistent spacing
    assert control_ids[0:4] == ["AC-1", "AC-2", "AC-2(1)", "AC-2 (2)"]


def test_implementation():
    parser = DocxParser(common.SOURCE_DOC)
    controls = parser.get_controls()

    control = controls["AC-1"]
    implementation = control.implementation["Part a"]
    assert "Microsoft Azure" in implementation
    assert "customer is responsible" in implementation
