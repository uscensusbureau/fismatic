from ..control_set import ControlSet
from ..demo import similar_implementations


def test_similar_implementations_empty():
    results = similar_implementations([], "foo", "a", "bar")
    assert results == []


def test_similar_implementations_excludes_blank():
    control = Control("AC-2")
    control.implementation = {"A": "     "}
    control_set = ControlSet([control], '')

    results = similar_implementations([control_set], "AC-2", "A", "foo")
    assert results == []


def test_similar_implementations():
    control1 = Control("AC-1")
    control1.implementation = {"A": "Something else."}
    control2 = Control("AC-2")
    imp1 = "This is about computers."
    control2.implementation = {"A": imp1}
    control_set1 = ControlSet([control1, control2], '')

    control3 = Control("AC-2")
    imp2 = "This is also about computers. Computers do a lot."
    control3.implementation = {"A": imp2}
    control_set2 = ControlSet([control3], '')

    control4 = Control("AC-2")
    imp3 = "Irrelevant."
    control4.implementation = {"A": imp3}
    control_set3 = ControlSet([control4], '')

    control_sets = [control_set1, control_set2, control_set3]

    results = similar_implementations(control_sets, "AC-2", "A", "computers")
    result_txt = [imp.text for imp in results]
    assert result_txt == [imp2, imp1, imp3]

