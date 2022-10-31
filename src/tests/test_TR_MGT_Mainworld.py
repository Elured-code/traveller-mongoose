import json
# from random import sample
import pytest
from src.TR_MGT_Mainworld import mainWorld
from src.utils.TR_MGT_Constants import TL_CAP


@pytest.fixture
def sample_set():
    '''Generate a sample set of mainworlds'''
    set = []
    for i in range(1, 100):
        m = mainWorld(str(i))
        m.loc = '0000'
        m.genWorld()
        set.append(m)

    return set


def test_mainWorld_name(sample_set):
    '''Test mainworld name assignment'''
    i = 0
    for w in sample_set:
        assert sample_set[i].worldname == str(i+1)
        i += 1


def test_mainWorld_starport(sample_set):
    '''Test starport generation'''
    i = 0
    for w in sample_set:
        assert sample_set[i].starPort in ['A', 'B', 'C', 'D', 'E', 'F', 'X']
        i += 1


def test_mainWorld_size(sample_set):
    '''Test size generation'''
    i = 0
    for w in sample_set:
        print(str(i))
        assert sample_set[i].siz in range(0, 11)
        i += 1


def test_mainWorld_atmosphere(sample_set):
    '''Test atmosphere generation value falls within bounds'''
    i = 0
    for w in sample_set:
        assert sample_set[i].atm in range(0, 16)
        i += 1


def test_mainWorld_hydrographics(sample_set):
    '''Test hydrographics generation value falls within bounds'''
    i = 0
    for w in sample_set:
        assert sample_set[i].hyd in range(0, 11)
        i += 1


def test_mainWorld_population(sample_set):
    '''Test population generation value falls within bounds'''
    i = 0
    for w in sample_set:
        assert sample_set[i].pop in range(0, 11)
        i += 1


def test_mainWorld_government(sample_set):
    '''Test government generation value falls within bounds'''
    i = 0
    for w in sample_set:
        assert sample_set[i].gov in range(0, 16)
        i += 1


def test_mainWorld_lawlevel(sample_set):
    '''Test law level generation fall within bounds'''
    i = 0
    for w in sample_set:
        assert sample_set[i].law in range(0, 16)
        i += 1


def test_mainWorld_techlevel(sample_set):
    '''Test tech level generation value falls within bounds'''
    for sample in sample_set:
        assert sample.tlv in range(0, 20)
        assert sample.tlv <= TL_CAP


def test_mainWorld_bases(sample_set):
    ''' Test base generation - ensure base code is 1 char only'''
    for sample in sample_set:
        assert len(sample.bases) == 1

# trade code tests will go here if needed


def test_mainWorld_population_mod(sample_set):
    '''Test that the population modifier is 1 - 9, except when pop = 0'''
    for sample in sample_set:
        if sample.pop > 0:
            assert sample.pMod > 0
        else:
            assert sample.pMod == 0


def test_mainWorld_belts(sample_set):
    '''Test for valied values for planetoid belts'''
    for sample in sample_set:
        assert sample.belts in (True, False)


def test_mainWorld_valid_JSON(sample_set):
    '''Test that the generated mainworld JSON file is valid'''
    for sample in sample_set:
        jsondoc = sample.createMainWorldJSON()
        try:
            json.loads(jsondoc)
        except ValueError:
            assert False
        else:
            assert True
