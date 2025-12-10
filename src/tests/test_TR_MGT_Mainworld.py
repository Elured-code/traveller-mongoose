# from random import sample

# pylint: disable=invalid-name
import pytest
from src.TR_MGT_Mainworld import MainWorld
from src.utils.TR_MGT_Constants import TL_CAP
# pylint: enable=invalid-name

@pytest.fixture
def pytest_configufre():
    """Generate a sample set of mainworlds"""
    new_set = []
    for i in range(1, 100):
        m = MainWorld(str(i))
        m.loc = "0000"
        m.gen_world()
        new_set.append(m)

    pytest.sample_set = new_set

def test_mainworld_name(sample_set):
    """Test mainworld name assignment"""
    i = 0
    for w in sample_set:
        assert w[i].worldname == str(i + 1)
        i += 1



def test_mainworld_starport(sample_set):
    """Test starport generation"""
    i = 0
    for w in sample_set:
        assert w[i].starPort in ["A", "B", "C", "D", "E", "F", "X"]
        i += 1



def test_mainworld_size(sample_set):
    """Test size generation"""
    i = 0
    for w in sample_set:
        print(str(i))
        assert w[i].siz in range(0, 11)
        i += 1



def test_mainworld_atmosphere(sample_set):
    """Test atmosphere generation value falls within bounds"""
    i = 0
    for w in sample_set:
        assert w[i].atm in range(0, 16)
        i += 1



def test_mainworld_hydrographics(sample_set):
    """Test hydrographics generation value falls within bounds"""
    i = 0
    for w in sample_set:
        assert w[i].hyd in range(0, 11)
        i += 1



def test_mainworld_population(sample_set):
    """Test population generation value falls within bounds"""
    i = 0
    for w in sample_set:
        assert w[i].pop in range(0, 11)
        i += 1



def test_mainworld_government(sample_set):
    """Test government generation value falls within bounds"""
    i = 0
    for w in sample_set:
        assert w[i].gov in range(0, 16)
        i += 1



def test_mainworld_lawlevel(sample_set):
    """Test law level generation fall within bounds"""
    i = 0
    for w in sample_set:
        assert w[i].law in range(0, 16)
        i += 1



def test_mainworld_techlevel(sample_set):
    """Test tech level generation value falls within bounds"""
    for sample in sample_set:
        assert sample.tlv in range(0, 20)
        assert sample.tlv <= TL_CAP



def test_mainworld_bases(sample_set):
    """Test base generation - ensure base code is 1 char only"""
    for sample in sample_set:
        assert len(sample.bases) == 1


# trade code tests will go here if needed

# def test_mainWorld_population_mod(sample_set):
#     '''Test that the population modifier is 1 - 9, except when pop = 0'''
#     for sample in sample_set:
#         if sample.pop > 0: assert sample.pMod > 0
#         else: assert sample.pMod == 0

# def test_mainWorld_belts(sample_set):
#     '''Test that the number of planetoid belts is valid'''
#     for sample in sample_set:
#         assert sample.nbelts in range(0, 10)


def test_mainworld_giants(sample_set):
    """Test if gas giants are generated correctly"""
    for sample in sample_set:
        assert sample.gas_giants in [True, False]
        