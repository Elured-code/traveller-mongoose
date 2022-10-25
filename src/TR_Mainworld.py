'''
    TR_Mainworld.py

    Abstract class to support future implementation of multiple generation
    systems using an object factory
'''

import abc
from abc import ABC, abstractmethod
import logging

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


class mainWorld(ABC):

    # Define properties

    @abc.abstractproperty
    def worldname(self):
        return self.__worldname

    @abc.abstractproperty
    def loc(self):
        return self.__loc

    @abc.abstractproperty
    def siz(self):
        return self.__siz

    @abc.abstractproperty
    def atm(self):
        return self.__atm

    @abc.abstractproperty
    def hyd(self):
        return self.__hyd

    @abc.abstractproperty
    def pop(self):
        return self.__pop

    @abc.abstractproperty
    def gov(self):
        return self.__gov

    @abc.abstractproperty
    def law(self):
        return self.__law

    @abc.abstractproperty
    def tlv(self):
        return self.__tlv

    @abc.abstractproperty
    def starPort(self):
        return self.__starPort

    @abc.abstractproperty
    def bases(self):
        return self.__bases

    @abc.abstractproperty
    def giants(self):
        return self.__giants

    @abc.abstractproperty
    def travelZone(self):
        return self.__travelZone

    @abc.abstractproperty
    def tradecodes(self):
        return self.__tradecodes

# Define setters, including checks
    @worldname.setter
    def worldname(self, worldname):
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

    @starPort.setter
    def starPort(self, starPort):
        self.__starPort = starPort

    @bases.setter
    def bases(self, bases):
        self.__bases = bases

    @travelZone.setter
    def travelZone(self, travelZone):
        self.__travelZone = travelZone

    @tradecodes.setter
    def tradecodes(self, tradecodes):
        self.__tradecodes = tradecodes

# Initialise the world class

    def __init__(self, wName):
        '''Takes a world name (wName) and initialises a mainworld object
            with that world name (self.worldname)'''

        logger.debug('Initialising world object with name %s', wName)

        # Initialise variables

        self.worldname = wName

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
    def gen_starPort(self, roll):
        pass

    @abstractmethod
    def gen_tlv(self, roll, tlcap):
        pass

    @abstractmethod
    def gen_bases(self):
        pass

    @abstractmethod
    def gen_travelZone(self, roll, isRandom):
        pass

    @abstractmethod
    def gen_belts(self, roll):
        pass

    @abstractmethod
    def gen_giants(self, roll1, roll2):
        pass

    @abstractmethod
    def gen_tradecodes(self):
        pass

    @abstractmethod
    def writemainWorldJSON(self):
        pass

# Randomly generate a mainworld object

    @abstractmethod
    def genWorld(self):
        pass

# Only execute if this code is called directly - used proimarily to debug
# output values


if __name__ == '__main__':
    w = mainWorld('Aworld')
    w.loc = "0101"
    w.genWorld()

    print(w)
    print(w.writemainWorldJSON())
