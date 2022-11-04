# from os import system
from src.utils import TR_MGT_Constants
from src.utils.TR_Support import D6Rollx2
from src import TR_MGT_Mainworld
import json


class System:

    @property
    def systemName(self):
        return self.__systemName

    @property
    def systemLocation(self):
        return self.__systemLocation

    @property
    def systemType(self):
        return self.__systemType

    @property
    def systemStars(self):
        return self.__systemStars

    @systemName.setter
    def systemName(self, systemName):
        self.__systemName = systemName

    @systemLocation.setter
    def systemLocation(self, systemLocation):
        self.__systemLocation = systemLocation

    @systemType.setter
    def systemType(self, systemType):
        self.__systemType = systemType

    @systemStars.setter
    def systemStars(self, systemStars):
        self.__systemStars = systemStars

    # Initialise the system class

    def __init__(self, sName):
        '''Takes a system name and initialises a system object'''

        # logger.debug('Initialising world object with name %s', sName)

        # Initialise variables

        self.systemName = sName
        self.systemStars = []

    def gen_systemType(self, roll):
        if roll == 2:
            x = D6Rollx2()
            if x == 2:
                y = D6Rollx2()
                self.systemType = \
                    TR_MGT_Constants.HIGHLY_UNUSUAL_SYSTEM_TYPE[y]
            else:
                self.systemType = TR_MGT_Constants.SPECIAL_SYSTEM_TYPE[x]
        else:
            self.__systemType = TR_MGT_Constants.SYSTEM_TYPE[roll]

    def gen_systemStars(self):
        '''Generate system primary objects - these are normally
           but not always stars'''

        starList = []

        # First set up the lists for each type of system

        # Solo stars

        if self.systemType == 'SOLO':
            starList.append({'Position': 'Primary', 'Orbits': None,
                            'Primary Distance': None})

        # Binary (Close)

        elif self.systemType == 'BINARY C':
            starList.append({'Position': 'Primary', 'Orbits': None,
                            'Orbit Distance': None})
            starList.append({'Position':  'Secondary', 'Orbits': 'Primary',
                            'Orbit Distance': 'Close'})

        # Binary (Distant)

        elif self.systemType == 'BINARY D':
            starList.append({'Position': 'Primary', 'Orbits': None,
                            'Orbit Distance': None})
            starList.append({'Position':  'Secondary', 'Orbits': 'Primary',
                            'Orbit Distance': 'Distant'})

        # Trinary (Close Secondary, Distant Tertiary)

        elif self.systemType == 'TRINARY C+D':
            starList.append({'Position': 'Primary', 'Orbits': None,
                            'Orbit Distance': None})
            starList.append({'Position':  'Secondary', 'Orbits': 'Primary',
                            'Orbit Distance': 'Close'})
            starList.append({'Position': 'Tertiary', 'Orbits': 'Primary',
                            'Orbit Distance': 'Distant'})

        # Trinary (Distant Secondary, Tertiary)

        elif self.systemType == 'TRINARY D+C':
            starList.append({'Position': 'Primary', 'Orbits': None,
                            'Orbit Distance': None})
            starList.append({'Position':  'Secondary', 'Orbits': 'Primary',
                            'Orbit Distance': 'Distant'})
            starList.append({'Position': 'Tertiary', 'Orbits': 'Secondary',
                            'Orbit Distance': 'Close'})

        # Other system types to come

        elif self.systemType == 'PRE-GIANT':

            # Using a custom table for pre-giant configuration

            thisConfiguration = \
                TR_MGT_Constants.PRE_GIANT_SYSTEM_TYPE(D6Rollx2())

            if thisConfiguration == 'SOLO':
                starList.append({'Position': 'Primary', 'Orbits': None,
                                'Primary Distance': None})
            elif thisConfiguration == 'BINARY C':
                starList.append({'Position': 'Primary', 'Orbits': None,
                                'Orbit Distance': None})
                starList.append({'Position':  'Secondary', 'Orbits': 'Primary',
                                'Orbit Distance': 'Close'})
            elif thisConfiguration == 'BINARY D':
                starList.append({'Position': 'Primary', 'Orbits': None,
                                'Orbit Distance': None})
                starList.append({'Position':  'Secondary', 'Orbits': 'Primary',
                                'Orbit Distance': 'Distant'})

        else:
            starList.append('Under Construction')
            self.systemStars = starList
            return

        # Now determiine the star types, starting with regular system types

        if self.systemType in ['SOLO', 'BINARY C', 'BINARY D', 'TRINARY C+D',
                               'TRINARY D+C', 'PRE-GIANT']:
            for thisStar in starList:

                if thisStar['Position'] == 'Primary':
                    x = D6Rollx2()

                    # No Brown Dwarf primaries for these system types

                    if x < 3:
                        x = 3

                elif thisStar['Orbit Distance'] == 'Close':
                    x = D6Rollx2() - 1
                elif thisStar['Orbit Distance'] == 'Distant':
                    x = D6Rollx2() - 2

                if x < 2:
                    x = 2

                if x == 12:

                    # Process A, B, O types

                    y = D6Rollx2()
                    thisStar['Spectral Class'] = \
                        TR_MGT_Constants.STAR_TYPES_ABO[y]
                    if thisStar['Spectral Class'] == 'Brown Dwarf':
                        thisStar['Star Type'] = None
                    else:
                        thisStar['Star Type'] = 'V'
                else:
                    thisStar['Spectral Class'] = \
                        TR_MGT_Constants.STAR_TYPES[x]
                    if thisStar['Spectral Class'] == 'Brown Dwarf':
                        thisStar['Star Type'] = None
                    else:
                        thisStar['Star Type'] = 'V'

                # Process close companions for pre-giant primaries

                if self.systemType == 'PRE-GIANT' and \
                   thisStar['Orbits'] == 'Primary' and \
                   thisStar['Orbit Distance'] == 'Close':
                    thisStar['Star Type'] += ' (Dying)'

        else:
            pass

        self.systemStars = starList

    def gen_MGT_System(self):
        self.gen_systemType(D6Rollx2())
        self.gen_systemStars()

    def createSystemObject(self):
        '''Create a JSON string that represents the system'''

        outputJSON = {}
        systemJSON = {}

        # Create the JSON header and populate

        headerJSON = {}
        headerJSON['Object Type'] = 'System'
        headerJSON['Rules System'] = TR_MGT_Constants.TR_SYSTEM
        headerJSON['Edition'] = TR_MGT_Constants.TR_SYSTEM_EDITION
        headerJSON['Version'] = TR_MGT_Constants.TR_SYSTEM_VERSION
        headerJSON['Extensions'] = TR_MGT_Constants.TR_SYSTEM_EXTENSIONS

        outputJSON['Header'] = headerJSON

        # Now write the system data to a dictionary object

        systemJSON['System Name'] = self.systemName
        systemJSON['System Location'] = self.systemLocation
        systemJSON['System Type'] = self.systemType

        # Add extension data here

        extensionData = {}

        systemJSON['Extension Data'] = extensionData

        # Add the system main bodies (stars)

        systemJSON['Stellar Objects'] = self.systemStars

        # Add any generated worlds

        # worldJSON = w.createMainWorldObject()
        # systemJSON['Worlds'] = [worldJSON]

        # Assemble the document parts

        outputJSON['System'] = systemJSON

        return outputJSON


if __name__ == '__main__':
    s = System('Test System')
    s.gen_MGT_System()
    s.systemLocation = '0101'

    w = TR_MGT_Mainworld.mainWorld(s.systemName)
    w.genWorld()
    w.loc = s.systemLocation
    print(json.dumps(s.createSystemObject(), indent=4))
