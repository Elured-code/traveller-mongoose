#
# T5 Constantds
#
#
# Author:   Michael Bailey
# Date:     1 November 2022
#

# Format metadata

TR_SYSTEM = "Traveller5"
TR_SYSTEM_EDITION = 5.10
TR_SYSTEM_VERSION = 2020
TR_SYSTEM_EXTENSIONS = [
    {
    }
]

# Define constants

STARPORTS = ["A", "B", "C", "D", "E", "X"]
STARPORT_FACILITIES = {
    "A": "Excellent",
    "B": "Good",
    "C": "Routine",
    "D": "Poor",
    "E": "Frontier",
    "X": "No Starport"
}

UWPCODETABLE = {
    0: "0", 1: "1", 2: "2",
    3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B",
    12: "C", 13: "D", 14: "E", 15: "F", 16: "G", 17: "H", 18: "J", 19: "K",
    20: "L", 21: "M"
}

# starPort code determination

STARPORTSTABLE = {
    2: "X", 3: "E", 4: "E", 5: "D", 6: "D", 7: "C", 8: "C", 9:
    "B", 10: "B", 11: "A", 12: "A"
}

# Home Star characteristics

HOMESTAR_TYPE = {
    -6: 'O', -5: 'B', -4: 'A', -3: 'A', -2: 'F', -1: 'F', 0: 'G', 1: 'K',
    2: 'K', 3: 'M', 4: 'M', 5: 'M', 6: 'M'
}

HOMESTAR_CLASSES = \
    {'O':
        {
            -6: 'Ia', -5: 'Ia', -4: 'Ib', -3: 'II', -2: 'III',
            -1: 'III', 0: 'III', 1: 'V', 2: 'V', 3: 'V', 4: 'IV',
            5: 'D', 6: 'D'
        },
        'B':
        {
            -6: 'Ia', -5: 'Ia', -4: 'Ib', -3: 'II', -2: 'III',
            -1: 'III', 0: 'III', 1: 'III', 2: 'V', 3: 'V', 4: 'IV',
            5: 'D', 6: 'D'
        },
        'A':
        {
            -6: 'Ia', -5: 'Ia', -4: 'Ib', -3: 'II', -2: 'III',
            -1: 'IV', 0: 'V', 1: 'V', 2: 'V', 3: 'V', 4: 'V',
            5: 'D', 6: 'D'
        },
        'F':
        {
            -6: 'II', -5: 'II', -4: 'III', -3: 'IV', -2: 'V',
            -1: 'V', 0: 'V', 1: 'V', 2: 'V', 3: 'V', 4: 'VI',
            5: 'D', 6: 'D'
        },
        'G':
        {
            -6: 'II', -5: 'II', -4: 'III', -3: 'IV', -2: 'V',
            -1: 'V', 0: 'V', 1: 'V', 2: 'V', 3: 'V', 4: 'VI',
            5: 'D', 6: 'D'
        },
        'K':
        {
            -6: 'II', -5: 'II', -4: 'III', -3: 'IV', -2: 'V',
            -1: 'V', 0: 'V', 1: 'V', 2: 'V', 3: 'V', 4: 'VI',
            5: 'D', 6: 'D'
        },
        'M':
        {
            -6: 'II', -5: 'II', -4: 'II', -3: 'II', -2: 'III',
            -1: 'V', 0: 'V', 1: 'V', 2: 'V', 3: 'V', 4: 'VI',
            5: 'D', 6: 'D'
        }
     }
