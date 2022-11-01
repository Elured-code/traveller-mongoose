# from random import sample
import pytest
from src import TR_MGT_System


@pytest.fixture
def sample_set():
    '''Generate a sample set of systems'''
    set = []
    for i in range(1, 100):
        s = TR_MGT_System.System(str(i))
        s.loc = '0000'
        set.append(s)

    return set


def test_System_name(sample_set):
    '''Test system name assignment'''
    i = 0
    for w in sample_set:
        assert sample_set[i].systemName == str(i+1)
        i += 1
