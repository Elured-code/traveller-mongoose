# from os import system
from src.utils import TR_MGT_Constants
from src.utils.TR_Support import D6Roll, D6Rollx2
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
    def systemGeometry(self):
        return self.__systemGeometry

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

    @systemGeometry.setter
    def systemGeometry(self, systemGeometry):
        self.__systemGeometry = systemGeometry

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

    def gen_systemGeometry(self):
        '''Generate system primary objects - these are normally
           but not always stars'''

        # First determine the system geometry, copying the system type for
        # non-special types

        if self.systemType in ['SOLO', 'BINARY C', 'BINARY D', 'TRINARY C+D',
                               'TRINARY D+C']:
            systemGeometry = self.systemType

        # Multiple stars

        elif self.systemType == 'MULTIPLE':
            systemGeometry = \
                TR_MGT_Constants.MULTIPLE_SYSTEM_GEOMETRY[D6Roll()]

        # Now determine the system geometry for special types

        # Pre-giant (subgiant) stars (Type IV)

        elif self.systemType == 'PRE-GIANT':
            systemGeometry = \
                TR_MGT_Constants.PRE_GIANT_SYSTEM_GEOMETRY[D6Rollx2()]

        # Giant stars - close companions are assumed to have been destroyed

        elif self.systemType == 'GIANT':
            systemGeometry = TR_MGT_Constants.GIANT_SYSTEM_GEOMETRY[D6Rollx2()]

        # Brown dwarfs

        elif self.systemType == 'BROWN DWARF':
            systemGeometry = \
                TR_MGT_Constants.BROWN_DWARF_SYSTEM_GEOMETRY[D6Roll()]

        # Empty systems
        # Note that these will need to be rerolled if the system is being
        # generated from a mailworld

        elif self.systemType == 'EMPTY':
            systemGeometry = 'EMPTY'

        # White dwarf stars - these stars do not have an inner system
        # or close companion, so use their own geometry table in
        # TR_MGT_Constants

        elif self.systemType == 'WHITE DWARF':
            pass

        else:
            systemGeometry = 'UNDER CONSTRUCTION'

        self.systemGeometry = systemGeometry

    def gen_MGT_System(self):
        self.gen_systemType(D6Rollx2())
        self.gen_systemGeometry()

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
        systemJSON['System Geometry'] = self.systemGeometry

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
