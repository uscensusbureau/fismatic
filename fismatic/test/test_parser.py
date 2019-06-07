import pytest
from .. import parser


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("control summary information", True),
        ("Control Summary Information", True),
        ("Control Enhancement Summary Information", True),
        ("something else", False),
    ],
)
def test_is_control_heading(test_input, expected):
    assert parser.is_control_heading(test_input) == expected
