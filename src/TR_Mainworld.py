'''
    TR_Mainworld.py

    Abstract class to support future implementation of multiple generation
    systems using an object factory
'''

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


class mainWorld:

    # Define properties

    @property
    def worldname(self):
        return self.__worldname

    @property
    def loc(self):
        return self.__loc

    @property
    def siz(self):
        return self.__siz

    @property
    def atm(self):
        return self.__atm

    @property
    def temperature(self):
        return self.__temperature

    @property
    def hyd(self):
        return self.__hyd

    @property
    def pop(self):
        return self.__pop

    @property
    def gov(self):
        return self.__gov

    @property
    def factions(self):
        return self.__factions

    @property
    def law(self):
        return self.__law

    @property
    def tlv(self):
        return self.__tlv

    @property
    def starPort(self):
        return self.__starPort

    @property
    def bases(self):
        return self.__bases

    @property
    def travelZone(self):
        return self.__travelZone

    @property
    def nbelts(self):
        return self.__nbelts

    @property
    def ngiants(self):
        return self.__ngiants

    @property
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

    @temperature.setter
    def temperature(self, temperature):
        self.__temperature = temperature

    @hyd.setter
    def hyd(self, hyd):
        self.__hyd = hyd

    @pop.setter
    def pop(self, pop):
        self.__pop = pop

    @gov.setter
    def gov(self, gov):
        self.__gov = gov

    @factions.setter
    def factions(self, factions):
        self.__factions = factions

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

    @nbelts.setter
    def nbelts(self, nbelts):
        self.__nbelts = nbelts

    @ngiants.setter
    def ngiants(self, ngiants):
        self.__ngiants = ngiants

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

    def gen_siz(self, roll):
        pass

    def gen_atm(self, roll):
        pass

    def gen_temperature(self, roll):
        pass

    def gen_hyd(self, roll):
        pass

    def gen_pop(self, roll):
        pass

    def gen_gov(self, roll):
        pass

    def gen_factions(self, roll):
        pass

    def gen_pMod(self, roll):
        pass

    def gen_law(self, roll):
        pass

    def gen_starPort(self, roll):
        pass

    def gen_tlv(self, roll, tlcap):
        pass

    def gen_bases(self):
        pass

    def gen_travelZone(self, roll, isRandom):
        pass

    def gen_nbelts(self, roll, roll2):
        pass

    def gen_ngiants(self, roll1, roll2):
        pass

    def gen_tradecodes(self):
        pass

    def writemainWorldJSON(self):
        pass

# Randomly generate a mainworld object

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
