import pytest
from ..control_set import ControlSet

@pytest.fixture
def sample_ssp():
    from ssp import SSP
    import os
    TEST_DIR = os.path.dirname(os.path.abspath(__file__))
    return SSP(TEST_DIR + '/test_files/test.docx')

def test_num_unique_implementations(sample_ssp):
    control_set = ControlSet(sample_ssp)
    assert control_set.num_unique_implementations() == 14


def test_num_tokens(sample_ssp):
    control_set = ControlSet(sample_ssp)
    assert control_set.num_tokens() == 29


def test_top_entities(sample_ssp):
    control_set = ControlSet(sample_ssp)
    assert control_set.top_entities()[0] == ("ac-1(a", 1)


def test_top_proper_noun_chunks(sample_ssp):
    control_set = ControlSet(sample_ssp)
    assert control_set.top_proper_noun_chunks()[0] == ("ac-1(a", 1)


def test_control_names(sample_ssp):
    control_set = ControlSet(sample_ssp)
    assert control_set.control_names() == ['AC-1', 'AC-2']
