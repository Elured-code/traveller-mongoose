# from random import sample
import pytest
from src import TR_MGT_System


@pytest.fixture
def sample_set():
    '''Generate a sample set of systems'''
    set = []
    for i in range(1, 1000):
        s = TR_MGT_System.System(str(i))
        s.loc = '0000'
        s.gen_MGT_System()
        set.append(s)

    return set


def test_system_systemName(sample_set):
    '''Test system name assignment'''
    i = 0
    for w in sample_set:
        assert sample_set[i].systemName == str(i+1)
        i += 1


def test_system_systemType(sample_set):
    for item in sample_set:
        assert item.systemType is not None


def test_system_starList(sample_set):
    pass
