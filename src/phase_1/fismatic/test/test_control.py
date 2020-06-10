import pytest
from ..control import Control


@pytest.mark.parametrize(
    "test_input,expected",
    [("AC-2", "AC-2"), ("AC-2 (1)", "AC-2 (1)"), ("AC-2(1)", "AC-2 (1)")],
)
def test_normalized_name(test_input, expected):
    control = Control(test_input)
    assert control.normalized_name() == expected
