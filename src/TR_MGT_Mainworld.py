import json
import logging
import math
from src.utils import TR_Constants, TR_MGT_Constants
from src.utils.TR_Support import D6Roll, D6Rollx2, D6Rollx3
import src.TR_Mainworld

# Configure logging

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(funcName)-20s \
                               %(levelname)-8s %(message)s',
                              '%d/%m/%Y %I:%M:%S %p')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.CRITICAL)

# mainWorld class - holds the world details as defined in the CE SRD


class mainWorld(src.TR_Mainworld.mainWorld):

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
    def belts(self):
        return self.__belts

    @property
    def nbelts(self):
        return self.__nbelts

    @property
    def giants(self):
        return self.__giants

    @property
    def ngiants(self):
        return self.__ngiants

    @property
    def tradecodes(self):
        return self.__tradecodes

# Define setters, including checks
    @worldname.setter
    def worldname(self, worldname):
        # if len(worldname) > 13:
        #     self.__worldname = worldname[0:13]
        self.__worldname = worldname
        logging.info('World name set to %s', self.__worldname)

    @loc.setter
    def loc(self, loc):
        # Add code here to check location value for suitability

        self.__loc = loc
        logging.info('World location set to %s', loc)

    @siz.setter
    def siz(self, siz):
        if siz < 0:
            self.__siz = 0
            logger.info('Size value %s out of bounds, setting to %s',
                        siz, self.__siz)
        elif siz > 10:
            self.__siz = 10
            logger.info('Size value %s out of bounds, setting to %s',
                        siz, self.__siz)
        else:
            self.__siz = siz

    @atm.setter
    def atm(self, atm):
        if atm < 0:
            self.__atm = 0
            logger.info('Atmosphere value %s out of bounds, setting to %s',
                        atm, self.__atm)
        elif atm > 15:
            self.__atm = 15
            logger.info('Atmosphere value %s out of bounds, setting to %s',
                        atm, self.__atm)
        else:
            self.__atm = atm

    @temperature.setter
    def temperature(self, temperature):
        if temperature not in TR_MGT_Constants.TEMPERATURES:
            logger.error("Temperature value %s not valid, \
                        setting to TEMPERATE", temperature)
            temperature = "TEMPERATE"
        self.__temperature = temperature

    @hyd.setter
    def hyd(self, hyd):
        if hyd < 0:
            self.__hyd = 0
            logger.info('Hydrographics value %s out of bounds, setting to %s',
                        hyd, self.__hyd)
        elif hyd > 10:
            self.__hyd = 10
            logger.info('Hydrographics value %s out of bounds, setting to %s',
                        hyd, self.__hyd)
        else:
            self.__hyd = hyd

    @pop.setter
    def pop(self, pop):
        if pop < 0:
            self.__pop = 0
            logger.info('Population value %s out of bounds, setting to %s',
                        pop, self.__pop)
        elif pop > 10:
            self.__pop = 10
        else:
            self.__pop = pop

    @gov.setter
    def gov(self, gov):
        if gov < 0:
            self.__gov = 0
            logger.info('Government value %s out of bounds, setting to %s',
                        gov, self.__gov)
        elif gov > 15:
            self.__gov = 15
            logger.info('Government value %s out of bounds, setting to %s',
                        gov, self.__gov)
        else:
            self.__gov = gov

    @factions.setter
    def factions(self, factions):
        self.__factions = factions

    @law.setter
    def law(self, law):
        if law < 0:
            self.__law = 0
            logger.info('Law level value %s out of bounds, setting to %s', law,
                        self.__law)
        elif law > 15:
            self.__law = 15
            logger.info('Law level value %s out of bounds, setting to %s', law,
                        self.__law)
        else:
            self.__law = law

    @tlv.setter
    def tlv(self, tlv):
        if tlv < 0:
            self.__tlv = 0
            logger.info('Tech level value %s out of bounds.  Setting to %s',
                        tlv, self.__tlv)
        else:
            self.__tlv = tlv

    @starPort.setter
    def starPort(self, starPort):
        if starPort in TR_Constants.STARPORTS:
            self.__starPort = starPort
        else:
            self.__starPort = "-"
            logger.info('Invalid value %s for starport code.  Setting to %s',
                        starPort, self.__starPort)

    @bases.setter
    def bases(self, bases):
        self.__bases = bases

    @travelZone.setter
    def travelZone(self, travelZone):
        self.__travelZone = travelZone

    @belts.setter
    def belts(self, belts):
        self.__belts = belts

    @nbelts.setter
    def nbelts(self, nbelts):
        self.__nbelts = nbelts
        if nbelts < 0:
            self.__nbelts = 0
            logger.info('Number of planetoid belts %s is out of bounds.  \
                        Setting to %s', nbelts, self.__nbelts)
        if nbelts > 3:
            self.__nbelts = 3
            logger.info('Number of planetoid belts %s is out of bounds.  \
                        Setting to %s', nbelts, self.__nbelts)

    @giants.setter
    def giants(self, giants):
        self.__giants = giants

    @ngiants.setter
    def ngiants(self, ngiants):
        self.__ngiants = ngiants
        if ngiants < 0:
            self.__ngiants = 0
            logger.info('Number of gas giants %s is out of bounds.  \
                        Setting to %s', ngiants, self.__ngiants)
        if ngiants > 4:
            self.__ngiants = 4
            logger.info('Number of gas giants %s is out of bounds.  \
                        Setting to %s', ngiants, self.__ngiants)

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

        # Capitalise the world name if it is a high population world

        if self.pop >= 9:
            self.worldname = self.worldname.upper()

        # Build the UWP String from the values generated above

        # Pad the world name with strings to column 13

        temp_worldname = "{:11.11}".format(self.worldname) + ' '

        returnstr = temp_worldname
        returnstr += self.loc + " "
        returnstr += self.starPort
        returnstr += TR_Constants.UWPCODETABLE.get(self.siz)
        returnstr += TR_Constants.UWPCODETABLE.get(self.atm)
        returnstr += TR_Constants.UWPCODETABLE.get(self.hyd)
        returnstr += TR_Constants.UWPCODETABLE.get(self.pop)
        returnstr += TR_Constants.UWPCODETABLE.get(self.gov)
        returnstr += TR_Constants.UWPCODETABLE.get(self.law)
        returnstr += "-" + TR_Constants.UWPCODETABLE.get(self.tlv)
        returnstr = returnstr + " " + self.bases

        # Format the trade code string

        tcode_string = ''
        for t in self.tradecodes:
            tcode_string += t + " "
        tcode_string.rstrip()

        returnstr += " " + tcode_string

        # Pad the UWP String with spaces to column 48

        returnstr = "{:<48}".format(returnstr)

        # Add the travel zone

        returnstr += "    "
        returnstr += self.travelZone
        returnstr += "  "

        # Add the PBG data

        returnstr += "  " + str(self.pMod) + str(self.nbelts) + \
            str(self.ngiants)

        # Add space for 2 character allegiance data

        returnstr += "    "

        # Star(s) type will go here

        return returnstr

    # Methods to randmomly generate mainworld properties

    def gen_siz(self, roll):
        '''Takes a dice roll (roll) and determines the mainworld
            size value (self.siz)'''

        logger.info('Generating size value for %s', self.worldname)
        x = roll - 2
        logger.debug('Result = %s', x)
        self.siz = x

    def gen_atm(self, roll):
        '''Takes a dice roll (roll) and determines the mainworld atmosphere
            value (self.atm) as a function of size (self.siz)'''

        logger.info('Generating atmosphere value for %s', self.worldname)
        x = roll + (self.siz - 7)
        if x < 0:
            x = 0
        elif x > 15:
            x = 15
        if self.siz == 0:
            x = 0
        logger.debug('Result = %s', x)
        self.atm = x

    def gen_temperature(self, roll):
        ''' Generate the world temperature class from input parameters and
            a random roll'''
        logger.info("Generating temperature value for %s", self.worldname)
        if self.atm <= 1:
            modifier = 0
        elif self.atm in [2, 3]:
            modifier = -2
        elif self.atm in [4, 5, 14]:
            modifier = -1
        elif self.atm in [6, 7]:
            modifier = 0
        elif self.atm in [8, 9]:
            modifier = 1
        elif self.atm in [10, 13, 15]:
            modifier = 2
        elif self.atm in [11, 12]:
            modifier = 6
        else:
            modifier = 0

        logger.debug("Roll = %s, Modifier = %s", roll, modifier)

        roll += modifier

        if roll <= 2:
            temperature = "FROZEN"
        elif roll in [3, 4]:
            temperature = "COLD"
        elif roll in [5, 6, 7, 8, 9]:
            temperature = "TEMPERATE"
        elif roll in [10, 11]:
            temperature = "HOT"
        elif roll >= 12:
            temperature = "BOILING"

        logger.info("Temperature = %s", temperature)
        self.temperature = temperature

    def gen_hyd(self, roll):
        '''Takes a dice roll (roll) and determines the mainworld hydrographics
            value (self.hyd) as a function of size (self.siz)'''

        logger.info('Generating hydrographics value for %s', self.worldname)
        x = roll + self.siz - 7

        if self.siz == 0:
            x = 0
        else:
            if self.atm in [0, 1, 10, 11, 12]:
                x -= 4
            if self.atm == 14:
                x -= 2
            if self.atm not in [13, 15]:
                if self.temperature == "HOT":
                    x -= 2
                elif self.temperature == "BOILING":
                    x -= 6
        if x < 0:
            x = 0
        if x > 10:
            x = 10
        logger.debug('Result = %s', x)
        self.hyd = x

    def gen_pop(self, roll):
        '''Takes a dice roll (roll) and determines the mainworld population
            value (self.pop).
            Note that in MGTv2 there are no modifiers for other attributes'''

        logger.info('Generating population value for %s', self.worldname)
        x = roll - 2
        if x < 0:
            x = 0
        if x > 12:
            x = 12

        logger.info('Result = %s', x)
        self.pop = x

    def gen_gov(self, roll):
        '''Takes a dice roll (roll) and determines the mainworld government
            value (self.gov) and a function of population (self.pop)'''
        logger.info('Generating government value for %s', self.worldname)
        x = roll - 7 + self.pop
        if self.pop == 0:
            x = 0
        logger.info('Result = %s', x)
        self.gov = x

    def gen_factions(self, roll):
        '''Determine the number and strength of factions in a mainworld
            government (Core Rules 2022 Update p254)'''

        logger.info('Generating factions for %s', self.worldname)
        factions = []

        # First get the number of factions

        x = math.floor(roll / 2)
        if self.gov in [0, 7]:
            x += 1
        if self.gov >= 10:
            x -= 1

        logger.info('Number of factions = %s', x)

        # Now determine the government type and strength of each faction
        # and store the details

        for y in range(x):
            thisFactionStrength = D6Rollx2()
            logging.debug("Faction %s strength = %s", y + 1,
                          thisFactionStrength)

            thisFactionGovType = D6Rollx2() - 7 + self.pop
            if self.pop == 0:
                thisFactionGovType = 0
            logging.debug("Faction %s government type roll = %s", y+1,
                          thisFactionGovType)
            if thisFactionGovType < 0:
                thisFactionGovType = 0
            factionDetail = {"Faction ID": y+1,
                             "Type":
                             TR_Constants.GOVERNMENTS[thisFactionGovType],
                             "Strength": thisFactionStrength}
            factions.append(factionDetail)

        logging.info("Factions determined: %s", factions)
        self.factions = factions

    def gen_pMod(self, roll):
        '''Takes a dice roll (roll) and determines the population multiplier
            value (self.pMod)'''

        logger.info('Generating population multiplier for %s', self.worldname)
        x = roll - 2
        if self.pop > 0 and x < 1:
            x = 1
        if self.pop == 0:
            x = 0
        if x == 10:
            x = 9
        logger.info('Result = %s', x)
        self.pMod = x

    def gen_law(self, roll):
        '''Takes a dice roll (roll) and determines the law level value
            (self.law) as a function of population (self.pop)'''

        logger.info('Generating law level value for %s', self.worldname)
        x = roll - 7 + self.gov
        if self.pop == 0:
            x = 0
            logger.info('No population, setting law level to 0')
        logger.info('Result = %s', x)
        self.law = x

    def gen_starPort(self, roll):
        '''Takes a dice roll (roll) and determines the starport type as a
            function of population (self.pop)'''

        logger.info('Generating starport type for %s', self.worldname)
        spRoll = roll - 7 + self.pop

        # Apply MGT modifiers based on mainworld population

        if self.pop in [8, 9]:
            spRoll += 1
        elif self.pop >= 10:
            spRoll += 2
        elif self.pop in [3, 4]:
            spRoll -= 1
        elif self.pop <= 2:
            spRoll -= 2

        if spRoll < 2:
            spRoll = 2
        if spRoll > 12:
            spRoll = 12

        logger.debug('Result = %s', spRoll)
        logger.info('Mainworld starport type is %s',
                    TR_Constants.STARPORTSTABLE[spRoll])

        self.starPort = TR_Constants.STARPORTSTABLE[spRoll]

    def gen_tlv(self, roll, tlcap):
        '''Takes a dice roll (roll) and determines the tech level value as a
            function of size (self.siz), hydrographics (self.hyd),
            atmosphere (self.atm), population (self.pop) and
            government (self.gov).
            TL will be capped at the value passed in tlcap'''

        logger.info('Generating tech level value for %s', self.worldname)
        if self.starPort in TR_Constants.STARPORTTLMOD:
            roll += TR_Constants.STARPORTTLMOD.get(self.starPort)
        if self.siz in TR_Constants.SIZETLMOD:
            roll += TR_Constants.SIZETLMOD.get(self.siz)
        if self.hyd in TR_Constants.HYDTLMOD:
            roll += TR_Constants.HYDTLMOD.get(self.hyd)
        if self.atm in TR_Constants.ATMTLMOD:
            roll += TR_Constants.ATMTLMOD.get(self.atm)
        if self.pop in TR_Constants.POPTLMOD:
            roll += TR_Constants.POPTLMOD.get(self.pop)
        if self.gov in TR_Constants.GOVTLMOD:
            roll += TR_Constants.GOVTLMOD.get(self.gov)

        # Add MGT world condition requirements for minimum TL

        if self.atm == 12:
            minTL = 10
        elif self.atm == 11:
            minTL = 9
        elif self.atm in [0, 1, 10, 15]:
            minTL = 8
        elif self.atm in [2, 3, 13, 14]:
            minTL = 5
        elif self.atm in [4, 7, 9]:
            minTL = 3
        else:
            minTL = 0

        if roll < minTL:
            roll = minTL

        # Finally, if population is zero, no TL

        if self.pop == 0:
            roll = 0

        logger.info('Result = %s', roll)

        self.tlv = roll

        if self.tlv > tlcap:
            logger.info('Capping TL value %s at %s', self.tlv, tlcap)
            self.tlv = tlcap

    def gen_bases(self):
        '''Takes 3 x dice rolls (roll1, roll2, roll3) and determines mainworld
            bases as a function of starport type (self.starPort)'''

        logger.info('Generating base codes for %s', self.worldname)

        # Check for Naval bases

        nBase = False
        if self.starPort == "A" or self.starPort == "B":
            if D6Rollx2() >= 8:
                nBase = True
            else:
                nBase = False

        # Scout bases / outposts

        sBase = False
        if self.starPort == "A":
            sBase = (D6Rollx2() >= 10)
        if self.starPort == "B":
            sBase = (D6Rollx2() >= 9)
        if self.starPort == "C":
            sBase = (D6Rollx2() >= 8)

        # Pirate bases

        pBase = False
        if self.starPort == "D":
            pBase = (D6Rollx2() == 12)
        if self.starPort in ["E", "X"]:
            pBase = (D6Rollx2() >= 10)

        # Format the base code

        bCode = " "
        if nBase and sBase:
            bCode = "A"
        if nBase and not sBase:
            bCode = "N"
        if sBase and pBase:
            bCode = "G"
        if pBase and not sBase:
            bCode = "P"
        if sBase and not nBase and not pBase:
            bCode = "S"

        logger.info('Result = %s', bCode)
        self.bases = bCode

    def gen_travelZone(self, roll, isRandom):
        '''Generate the mainworld travel zone'''

        logger.info('Generating travel zone for %s', self.worldname)

        travelZone = ' '

        # Check for amber zone

        if (self.atm >= 10) or (self.gov in [0, 7, 10]) or (self.law == 0) or \
           (self.law >= 9):
            logger.debug('Checking for amber zone based on atm, gov, law)')
            if D6Roll() > 3:
                logger.debug('Travel zone set to A')
                travelZone = 'A'

        # Now add some random zone generation if the random flag is set

        if isRandom and travelZone == ' ':
            logger.debug('Random travel zone generation is set, generating \
                        travel zones')
            x = D6Rollx3()
            logger.debug('Roll = %s', x)
            if x >= 16:
                travelZone = 'A'
            if x == 18:
                travelZone = 'R'

        else:
            logger.debug('Random travel zone generation is not set')

        logger.info('Travel zone set to %s', travelZone)

        self.travelZone = travelZone

    def gen_belts(self, roll):
        if roll >= 10:
            belts = True
        else:
            belts = False
        self.__belts = belts

    def gen_giants(self, roll):
        if roll >= 7:
            giants = True
        else:
            giants = False
        self.__giants = giants

    def gen_nbelts(self, roll, roll2):
        '''Takes 2 x dice rolls (roll1, roll2) and determines the number of
            planetoid belts as a function of size (self.siz)'''

        logger.info('Generating planetoid belts for %s', self.worldname)

        # Determine the presence of planetoid belts

        nbelts = 0
        if roll >= 4:
            nbelts = roll2 - 3
            if self.__siz == 0 and nbelts < 1:
                nbelts = 1
                logger.info('Mainworld size is 0 but no belts present.  \
                    Setting number of belts to %s', nbelts)

        logger.info('Result = %s', nbelts)
        self.nbelts = nbelts

    def gen_ngiants(self, roll1, roll2):
        '''Takes 2 x dice rolls (roll1, roll2) and determines the number of
            gas giants'''

        logger.info('Generating gas giants for %s', self.worldname)

        # Determine the presence of gas giants

        if D6Rollx2() >= 5:
            ngiants = (D6Roll() - 2)
            if ngiants < 1:
                ngiants = 1
        else:
            ngiants = 0
        logger.info('Result = %s', ngiants)
        self.ngiants = ngiants

    def gen_tradecodes(self):
        '''Determines the mainworld trade codes from attribute values'''

        logger.info('Determining trade codes for %s', self.worldname)

        # Generate trade codes

        tcode = []
        if self.atm >= 4 and self.atm <= 9 and self.hyd >= 4 and self.hyd <= 8\
           and self.pop >= 5 and self.pop <= 7:
            tcode.append("Ag")
        if self.siz == 0 and self.atm == 0 and self.hyd == 0:
            tcode.append("As")
        if self.pop == 0 and self.gov == 0 and self.law == 0:
            tcode.append("Ba")
        if self.atm >= 2 and self.hyd == 0:
            tcode.append("De")
        if self.atm >= 10 and self.hyd >= 1:
            tcode.append("Fl")
        if self.atm in [5, 6, 8] and\
           self.hyd >= 4 and self.hyd <= 9 and\
           self.pop >= 4 and self.pop <= 8:
            tcode.append("Ga")
        if self.pop >= 9:
            tcode.append("Hi")
        if self.tlv >= 12:
            tcode.append("Ht")
        if self.atm in [0, 1] and self.hyd >= 1:
            tcode.append("Ic")
        if self.atm in [0, 1, 2, 4, 7, 9] and self.pop >= 9:
            tcode.append("In")
        if self.pop >= 1 and self.pop <= 3:
            tcode.append("Lo")
        if self.tlv <= 5:
            tcode.append("Lt")
        if self.atm <= 3 and self.hyd <= 3 and self.pop >= 6:
            tcode.append("Na")
        if self.pop >= 4 and self.pop <= 6:
            tcode.append("Ni")
        if self.atm >= 2 and self.atm <= 5 and self.hyd <= 3:
            tcode.append("Po")
        if self.atm in [6, 8] and self.pop >= 6 and self.pop <= 8:
            tcode.append("Ri")
        if self.hyd == 10:
            tcode.append("Wa")
        if self.atm == 0:
            tcode.append("Va")

        logger.info('Generated trade codes = %s', tcode)
        self.tradecodes = tcode

    def writemainWorldJSON(self):
        '''Write mainworld to a JSON document'''

        outputJSON = {}
        mainWorldJSON = {}

        # Create the JSON header and populate

        headerJSON = {}
        headerJSON['Rules System'] = TR_MGT_Constants.TR_SYSTEM
        headerJSON['Edition'] = TR_MGT_Constants.TR_SYSTEM_EDITION
        headerJSON['Version'] = TR_MGT_Constants.TR_SYSTEM_VERSION
        headerJSON['Extensions'] = TR_MGT_Constants.TR_SYSTEM_EXTENSIONS

        outputJSON['Header'] = headerJSON

        # Now write the mainworld data to a dictionary object

        mainWorldJSON['Name'] = self.worldname
        mainWorldJSON['UWP'] = str(self)
        mainWorldJSON['Starport'] = self.starPort
        mainWorldJSON['Size'] = self.siz
        mainWorldJSON['Atmosphere'] = self.atm
        mainWorldJSON['Hydrographics'] = self.hyd
        mainWorldJSON['Population'] = self.pop
        mainWorldJSON['Goverment'] = self.gov
        mainWorldJSON['Law Level'] = self.law
        mainWorldJSON['Tech Level'] = self.tlv
        mainWorldJSON['Bases'] = self.bases
        mainWorldJSON['Trade Codes'] = self.tradecodes
        mainWorldJSON['Population Modifier'] = self.pMod
        mainWorldJSON['Planetoid Belts'] = self.nbelts
        mainWorldJSON['Gas Giants'] = self.ngiants

        # Add extension data here

        extensionData = {}
        extensionData['Government Factions'] = self.factions
        extensionData['PBG Data'] = {'Population Multiplier': self.pMod,
                                     'Belts': self.nbelts,
                                     'Giants': self.ngiants}

        mainWorldJSON['Extension Data'] = extensionData

        # Assemble the document parts

        outputJSON['Contents'] = mainWorldJSON

        outjson = json.dumps(outputJSON, indent=4)
        return outjson

# Randomly generate a mainworld object

    def genWorld(self):
        '''Generate attribute values for a mainworld object'''
        logger.info('Generating world data for %s', self.worldname)

        # Generate world data

        # Generate physical stats

        self.gen_siz(D6Rollx2())
        self.gen_atm(D6Rollx2())
        self.gen_temperature(D6Rollx2())
        self.gen_hyd(D6Rollx2())
        self.gen_pop(D6Rollx2())
        self.gen_pMod(D6Rollx2())
        self.gen_gov(D6Rollx2())
        self.gen_factions(D6Rollx2())
        self.gen_law(D6Rollx2())
        self.gen_starPort(D6Rollx2())
        self.gen_tlv(D6Roll(), TR_MGT_Constants.TL_CAP)
        self.gen_bases()
        self.gen_travelZone(D6Rollx2, True)
        self.gen_nbelts(D6Rollx2(), D6Roll())
        self.gen_ngiants(D6Rollx2(), D6Roll())
        self.gen_tradecodes()

# Only execute if this code is called directly - used proimarily to debug
# output values


if __name__ == '__main__':
    w = mainWorld('Aworld')
    w.loc = "0101"
    w.genWorld()

    print(w)
    print(w.writemainWorldJSON())
