#
# Mongoose Traveller 2E 2022 constants
#
#
# Author:   Michael Bailey
# Date:
#

# Define constants

# Decimal to Traveller Hex Code translation
# Note that in non-Book 3 implementations this is extended out, skipping "I"
# and "O"

# Format metadata

TR_SYSTEM = "Mongoose Traveller"
TR_SYSTEM_EDITION = 2
TR_SYSTEM_VERSION = 2022
TR_SYSTEM_EXTENSIONS = [
    {
    }

]

UWPCODETABLE = {0: "0", 1: "1", 2: "2",
                3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
                10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F",
                16: "G", 17: "H", 18: "J", 19: "K", 20: "L", 21: "M"}

# System type codes

SYSTEM_TYPE = {2: "SPECIAL",
               3: "TRINARY C+D",
               4: "TRINARY C+D",
               5: "BINARY C",
               6: "BINARY C",
               7: "SOLO",
               8: "SOLO",
               9: "BINARY D",
               10: "BINARY D",
               11: "TRINARY D+C",
               12: "MULTIPLE"}

SPECIAL_SYSTEM_TYPE = {2: "HIGHLY UNUSUAL",
                       3: "PRE-GIANT",
                       4: "BROWN DWARF",
                       5: "BROWN DWARF",
                       6: "EMPTY",
                       7: "EMPTY",
                       8: "EMPTY",
                       9: "WHITE DWARF",
                       10: "WHITE DWARF",
                       11: "GIANT",
                       12: "UNSTABLE"}

HIGHLY_UNUSUAL_SYSTEM_TYPE = {2: "BLACK HOLE",
                              3: "ANOMALY",
                              4: "ANOMALY",
                              5: "NEBULA / PROTOSTAR",
                              6: "NEBULA / PROTOSTAR",
                              7: "NEBULA / PROTOSTAR",
                              8: "NEBULA / PROTOSTAR",
                              9: "NEBULA / PROTOSTAR",
                              10: "HIGHLY COMPLEX",
                              11: "HIGHLY COMPLEX",
                              12: "NEUTRON STAR"}

STAR_TYPES = {0: "Brown Dwarf",
              1: "Brown Dwarf",
              2: "Brown Dwarf",
              3: "M",
              4: "M",
              5: "M",
              6: "M",
              7: "K",
              8: "K",
              9: "G",
              10: "G",
              11: "F",
              12: "A/B/O"}

STAR_TYPES_ABO = {1: "A",
                  2: "A",
                  3: "A",
                  4: "B",
                  5: "B",
                  6: "O"}

MAIN_SEQ_CARDINALITY = ['O', 'B', 'A', 'F', 'G', 'K', 'M']

# This is new, not in the DSE handbook explicitly

MULTIPLE_SYSTEM_GEOMETRY = {
    1: "QUAD C, D+C",
    2: "QUAD C, D+C",
    3: "QUAD C, D+C",
    4: "QUAD D+C, D",
    5: "QUAD D+C, D",
    6: "QUAD D, D, D"
}

# This is new, not in the DSE handbook explicitly

PRE_GIANT_SYSTEM_GEOMETRY = {2: "BINARY C",
                             3: "TRINARY D+C",
                             4: "BINARY D",
                             5: "BINARY D",
                             6: "SOLO",
                             7: "SOLO",
                             8: "SOLO",
                             9: "SOLO",
                             10: "BINARY D",
                             11: "TRINARY D+C",
                             12: "TRINARY C+D"}

# This is new, not in the DSE handbook explicitly

GIANT_SYSTEM_GEOMETRY = {2: "TRINARY D+C",
                         3: "TRINARY D+C",
                         4: "BINARY D",
                         5: "BINARY D",
                         6: "SOLO",
                         7: "SOLO",
                         8: "SOLO",
                         9: "SOLO",
                         10: "BINARY D",
                         11: "BINARY D",
                         12: "TRINARY D+C"}

# This is new, not in the DSE handbook explicitly

BROWN_DWARF_SYSTEM_GEOMETRY = {
    1: "TRINARY C+D",
    2: "BINARY C",
    3: "SOLO",
    4: "SOLO",
    5: "BINARY D",
    6: "TRINARY C+D"
}

# Starport codes

STARPORTS = ["A", "B", "C", "D", "E", "X"]

# Temperature values

TEMPERATURES = ["FROZEN", "COLD", "TEMPERATE", "HOT", "BOILING"]

# Define the maximum allowed tech level

TL_CAP = 15
