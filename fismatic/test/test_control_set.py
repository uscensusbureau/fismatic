from . import common
from ..control import Control
from ..control_set import ControlSet


def test_num_words():
    control1 = Control("foo")
    control1.implementation = {"A": "foo does things"}

    control2 = Control("bar")
    control2.implementation = {"A": "bar does things"}

    control_set = ControlSet([control1, control2])
    assert control_set.num_words() == 6
