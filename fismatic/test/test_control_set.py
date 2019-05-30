from ..control import Control
from ..control_set import ControlSet


def test_num_tokens():
    control1 = Control("foo")
    control1.implementation = {"A": "foo - does things"}

    control2 = Control("bar")
    control2.implementation = {"A": "bar's a thinger do-er"}

    control_set = ControlSet([control1, control2])
    assert control_set.num_tokens() == 9


def test_all_tokens():
    control1 = Control("foo")
    control1.implementation = {"A": "foo - does things"}

    control2 = Control("bar")
    control2.implementation = {"A": "bar's a thinger do-er"}

    control_set = ControlSet([control1, control2])
    assert control_set.all_tokens() == [
        "foo",
        "does",
        "things",
        "bar",
        "a",
        "thinger",
        "do-er",
    ]
