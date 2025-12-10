'''
    TR_Mainworld.py

    Abstract class to support future implementation of multiple generation
    systems using an object factory
'''
# pylint: disable=invalid-name
from abc import ABC, abstractmethod
import logging
# pylint: enable=invalid-name

# Configure logging

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(funcName)-20s \
                               %(levelname)-8s %(message)s',
                              '%d/%m/%Y %I:%M:%S %p')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.CRITICAL)

# mainWorld abstract class


class MainWorld(ABC):

    # Define properties

    @property
    @abstractmethod
    def world_name(self):
        return self.__worldname

    @property
    @abstractmethod
    def loc(self):
        return self.__loc
    @property
    @abstractmethod
    def siz(self):
        return self.__siz

    @property
    @abstractmethod
    def atm(self):
        return self.__atm

    @property
    @abstractmethod
    def hyd(self):
        return self.__hyd

    @property
    @abstractmethod
    def pop(self):
        return self.__pop

    @property
    @abstractmethod
    def gov(self):
        return self.__gov

    @property
    @abstractmethod
    def law(self):
        return self.__law

    @property
    @abstractmethod
    def tlv(self):
        return self.__tlv

    @property
    @abstractmethod
    def star_port(self):
        return self.__star_port

    @property
    @abstractmethod
    def bases(self):
        return self.__bases

    @property
    @abstractmethod
    def belts(self):
        return self.__belts

    @property
    @abstractmethod
    def giants(self):
        return self.__giants

    @property
    @abstractmethod
    def travel_zone(self):
        return self.__travel_zone

    @property
    @abstractmethod
    def tradecodes(self):
        return self.__tradecodes

# Define setters, including checks
    @world_name.setter
    def world_name(self, worldname):
        self.__worldname = worldname

    @loc.setter
    def loc(self, loc):
        self.__loc = loc

    @siz.setter
    def siz(self, siz):
        self.__siz = siz

    @atm.setter
    def atm(self, atm):
        self.__atm = atm

    @hyd.setter
    def hyd(self, hyd):
        self.__hyd = hyd

    @pop.setter
    def pop(self, pop):
        self.__pop = pop

    @gov.setter
    def gov(self, gov):
        self.__gov = gov

    @law.setter
    def law(self, law):
        self.__law = law

    @tlv.setter
    def tlv(self, tlv):
        self.__tlv = tlv

    @star_port.setter
    def star_port(self, star_port):
        self.__star_port = star_port

    @belts.setter
    def belts(self, belts):
        self.__belts = belts

    @giants.setter
    def giants(self, giants):
        self.__giants = giants

    @bases.setter
    def bases(self, bases):
        self.__bases = bases

    @travel_zone.setter
    def travel_zone(self, travel_zone):
        self.__travel_zone = travel_zone

    @tradecodes.setter
    def tradecodes(self, tradecodes):
        self.__tradecodes = tradecodes

# Initialise the world class

    def __init__(self, world_name):
        '''Takes a world name (wName) and initialises a mainworld object
            with that world name (self.worldname)'''

        logger.debug('Initialising world object with name %s', world_name)

        # Initialise variables

        self.world_name = world_name

    # Display the mainworld object as a string

    def __str__(self):
        pass

    # Methods to randmomly generate mainworld properties

    @abstractmethod
    def gen_siz(self, roll):
        pass

    @abstractmethod
    def gen_atm(self, roll):
        pass

    @abstractmethod
    def gen_temperature(self, roll):
        pass

    @abstractmethod
    def gen_hyd(self, roll):
        pass

    @abstractmethod
    def gen_pop(self, roll):
        pass

    @abstractmethod
    def gen_gov(self, roll):
        pass

    @abstractmethod
    def gen_law(self, roll):
        pass

    @abstractmethod
    def gen_starport(self, roll):
        pass

    @abstractmethod
    def gen_tlv(self, roll, tlcap):
        pass

    @abstractmethod
    def gen_bases(self):
        pass

    @abstractmethod
    def gen_travel_zone(self, roll, is_random):
        pass

    @abstractmethod
    def gen_belts(self, roll):
        pass

    @abstractmethod
    def gen_giants(self, roll):
        pass

    @abstractmethod
    def gen_tradecodes(self):
        pass

    @abstractmethod
    def create_mainworld_json(self):
        pass

# Randomly generate a mainworld object

    @abstractmethod
    def gen_world(self):
        pass
