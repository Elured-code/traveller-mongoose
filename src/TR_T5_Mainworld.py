import json
import logging
import this
from src.utils import TR_Constants, TR_T5_Constants
from src.utils.TR_Support import D6Roll, D6Rollx2, D6Rollx3, FluxRoll, D10Roll
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


# class mainWorld(src.TR_Mainworld.mainWorld):
class mainWorld():
    # Define properties

    @property
    def worldname(self):
        return self.__worldname

    @property
    def loc(self):
        return self.__loc

    @property
    def starPort(self):
        return self.__starPort

    @property
    def homeStar(self):
        return self.__homeStar

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

    @starPort.setter
    def starPort(self, starPort):
        if starPort in TR_Constants.STARPORTS:
            self.__starPort = starPort
        else:
            self.__starPort = "-"
            logger.info('Invalid value %s for starport code.  Setting to %s',
                        starPort, self.__starPort)

    @homeStar.setter
    def homeStar(self, homeStar):
        self.__homeStar = homeStar

# Initialise the world class

    def __init__(self, wName):
        '''Takes a world name (wName) and initialises a mainworld object
            with that world name (self.worldname)'''

        logger.debug('Initialising world object with name %s', wName)

        # Initialise variables

        self.worldname = wName
        self.homeStar = {}

    # Display the mainworld object as a string

    def __str__(self):

        # Capitalise the world name if it is a high population world

        # if self.pop >= 9:
        #     self.worldname = self.worldname.upper()

        # Build the UWP String from the values generated above

        # Pad the world name with strings to column 13

        temp_worldname = "{:11.11}".format(self.worldname) + ' '

        returnstr = temp_worldname
        returnstr += self.loc + " "
        returnstr += self.starPort
        # returnstr += TR_Constants.UWPCODETABLE.get(self.siz)
        # returnstr += TR_Constants.UWPCODETABLE.get(self.atm)
        # returnstr += TR_Constants.UWPCODETABLE.get(self.hyd)
        # returnstr += TR_Constants.UWPCODETABLE.get(self.pop)
        # returnstr += TR_Constants.UWPCODETABLE.get(self.gov)
        # returnstr += TR_Constants.UWPCODETABLE.get(self.law)
        # returnstr += "-" + TR_Constants.UWPCODETABLE.get(self.tlv)
        # returnstr = returnstr + " " + self.bases

        # # Format the trade code string

        # tcode_string = ''
        # for t in self.tradecodes:
        #     tcode_string += t + " "
        # tcode_string.rstrip()

        # returnstr += " " + tcode_string

        # # Pad the UWP String with spaces to column 48

        # returnstr = "{:<48}".format(returnstr)

        # # Add the travel zone

        # returnstr += "    "
        # returnstr += self.travelZone
        # returnstr += "  "

        # # Add space for 2 character allegiance data - this will be improved
        # # at a later date to match T5 requirements (probably)

        # returnstr += self.allegiance
        # returnstr += "  "

        # # Star(s) type will go here

        return returnstr

    # Methods to randmomly generate mainworld properties

    def gen_starPort(self, roll):
        '''Takes a dice roll (roll) and determines the starport type'''

        logger.info('Generating starport type for %s', self.worldname)
        self.starPort = TR_Constants.STARPORTSTABLE[roll]
        logger.info('Mainworld starport type is %s', self.starPort)

    def gen_homeStar(self, roll, roll2, roll3):
        thisStar = {}
        logger.info('Generating home star stellar type')
        thisStar['Stellar Type'] = TR_T5_Constants.HOMESTAR_TYPE[roll]
        logger.info('Home star type = %s', thisStar['Stellar Type'])

        logger.info('Generating home star luminosity')
        thisStar['Luminosity'] = roll3 - 1

        logger.info('Generating home star class')
        starTypes = TR_T5_Constants.HOMESTAR_CLASSES[thisStar['Stellar Type']]
        thisStar['Stellar Class'] = starTypes[roll2]

        # Process exclusions

        if thisStar['Stellar Type'] == 'IV':
            if thisStar['Stellar Class'] in ['K', 'M']:
                thisStar['Stellar Type'] = 'V'

        if thisStar['Stellar Type'] == 'VI':
            if thisStar['Stellar Class'] == 'A':
                thisStar['Stellar Type'] = 'V'
            elif thisStar['Stellar Class'] == 'F' and thisStar['Luminosity'] \
                    in range(0, 5):
                thisStar['Stellar Type'] == 'V'

        # Remove luminosity value for dwarf stars

        if thisStar['Stellar Type'] == 'D':
            del thisStar['Luminosity']

        self.homeStar = thisStar

    def createMainWorldJSON(self):
        '''Create a JSON string that represents the mainworld data'''

        outputJSON = {}
        mainWorldJSON = {}

        # Create the JSON header and populate

        headerJSON = {}
        headerJSON['Object Type'] = 'Main World'
        headerJSON['Rules System'] = TR_T5_Constants.TR_SYSTEM
        headerJSON['Edition'] = TR_T5_Constants.TR_SYSTEM_EDITION
        headerJSON['Version'] = TR_T5_Constants.TR_SYSTEM_VERSION
        headerJSON['Extensions'] = TR_T5_Constants.TR_SYSTEM_EXTENSIONS

        outputJSON['Header'] = headerJSON

        # Now write the mainworld data to a dictionary object

        mainWorldJSON['Name'] = self.worldname
        mainWorldJSON['Home Star'] = self.homeStar
        mainWorldJSON['UWP'] = str(self)
        mainWorldJSON['Starport'] = self.starPort

        # Add extension data here

        extensionData = {}

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

        # Step 1a - Generate Starport

        self.gen_starPort(D6Rollx2())

        # Step 2a - Home Star

        self.gen_homeStar(FluxRoll(), FluxRoll(), D10Roll())

# Only execute if this code is called directly - used proimarily to debug
# output values


if __name__ == '__main__':
    w = mainWorld('Aworld')
    w.loc = "0101"
    w.genWorld()
    print(w)
    print(w.createMainWorldJSON())

    # Test write JSON to file

    # outJSON = w.createMainWorldJSON()

    # with open('output.json', 'w') as json_file:
    #     json_file.write(outJSON)

    # # Test read JSON from file

    # with open('output.json', 'r') as json_file:
    #     inputJSON = json_file.read()

    # print(inputJSON)
