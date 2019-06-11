import os.path
import pytest
from . import common
from .. import core as fismatic


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (common.SOURCE_DOC, [common.SOURCE_DOC]),  # single file
        (".", [common.SOURCE_DOC]),  # directory with docx
        ("fismatic", []),  # directory without docx
    ],
)
def test_get_files(test_input, expected):
    result = fismatic.get_files(test_input)

    # absolute-ize the paths so that it doesn't fail due to leading `./`s
    result = [os.path.abspath(p) for p in result]
    expected = [os.path.abspath(p) for p in expected]

    assert result == expected
