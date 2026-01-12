'''
    test_TR_MGT_Mainworld.py

    Abstract class to support future implementation of multiple generation
    systems using an object factory
'''

# pylint: disable=invalid-name

from src.tr_mgt_mainword import MainWorld
from src.utils.TR_MGT_Constants import TL_CAP
# pylint: enable=invalid-name

# pylint: disable=unused-import

def sample_set():
    """Generate a sample set of mainworlds"""
    new_set = []
    for i in range(1, 100):
        m = MainWorld(str(i))
        m.loc = "0000"
        m.gen_world()
        new_set.append(m)

    return new_set

a_set = sample_set()

def test_mainworld_name():
    """Test mainworld name assignment"""

    # Grab the sample set

    this_set = a_set

    i = 0
    for w in this_set:
        assert w.world_name == str(i + 1)
        i += 1



def test_mainworld_starport():
    """Test starport generation"""

    # Grab the sample set

    this_set = a_set

    i = 0
    for w in this_set:
        assert w.star_port in ["A", "B", "C", "D", "E", "F", "X"]
        i += 1



def test_mainworld_size():
    """Test size generation"""

    # Grab the sample set

    this_set = a_set

    i = 0
    for w in this_set:
        print(str(i))
        assert w.siz in range(0, 11)
        i += 1



def test_mainworld_atmosphere():
    """Test atmosphere generation value falls within bounds"""

    # Grab the sample set

    this_set = a_set

    i = 0
    for w in this_set:
        assert w.atm in range(0, 16)
        i += 1



def test_mainworld_hydrographics():
    """Test hydrographics generation value falls within bounds"""

    # Grab the sample set

    this_set = a_set

    i = 0
    for w in this_set:
        assert w.hyd in range(0, 11)
        i += 1

def test_mainworld_population():
    """Test population generation value falls within bounds"""

    # Grab the sample set

    this_set = a_set

    # Grab the sample set

    this_set = a_set

    i = 0
    for w in this_set:
        assert w.pop in range(0, 11)
        i += 1



def test_mainworld_government():
    """Test government generation value falls within bounds"""

    # Grab the sample set

    this_set = a_set

    i = 0
    for w in this_set:
        assert w.gov in range(0, 16)
        i += 1



def test_mainworld_lawlevel():
    """Test law level generation fall within bounds"""

    # Grab the sample set

    this_set = a_set

    i = 0
    for w in this_set:
        assert w.law in range(0, 16)
        i += 1



def test_mainworld_techlevel():
    """Test tech level generation value falls within bounds"""

    # Grab the sample set

    this_set = a_set

    for sample in this_set:
        assert sample.tlv in range(0, 20)
        assert sample.tlv <= TL_CAP



def test_mainworld_bases():
    """Test base generation - ensure base code is 1 char only"""

    # Grab the sample set

    this_set = a_set

    for sample in this_set:
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


def test_mainworld_giants():
    """Test if gas giants are generated correctly"""

    # Grab the sample set

    this_set = a_set

    for sample in this_set:
        assert sample.giants in [True, False]
        