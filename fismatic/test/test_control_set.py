from ..control import Control
from ..control_set import ControlSet


def test_num_tokens():
    control1 = Control("foo")
    control1.implementation = {"A": "foo - does things"}

    control2 = Control("bar")
    control2.implementation = {"A": "bar's a thinger do-er"}

    control_set = ControlSet([control1, control2])
    assert control_set.num_tokens() == 9


def test_top_entities():
    control1 = Control("foo")
    control1.implementation = {
        "A": "FISMATic is the greatest thing to happen to the United States since sliced bread."
    }

    control2 = Control("bar")
    control2.implementation = {"A": "Have I told you how great FISMAtic is?"}

    control_set = ControlSet([control1, control2])

    # TODO this should have captured "FISMAtic"
    assert control_set.top_entities() == [("the United States", 1)]


def test_top_proper_noun_chunks():
    control1 = Control("foo")
    control1.implementation = {
        "A": "FISMATic is the greatest thing to happen to the United States since sliced bread."
    }

    control2 = Control("bar")
    control2.implementation = {"A": "Have I told you how great FISMAtic is?"}

    control_set = ControlSet([control1, control2])

    # TODO this should have captured "FISMAtic"
    assert control_set.top_proper_noun_chunks() == [("the United States", 1)]


def test_control_names():
    control1 = Control("AC-2")
    control1.implementation = {"": ""}
    control2 = Control("AU-6(1)")
    control2.implementation = {"": ""}
    control_set = ControlSet([control1, control2])

    assert control_set.control_names() == ["AC-2", "AU-6 (1)"]
