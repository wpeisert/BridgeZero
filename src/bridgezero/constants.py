# declare constants

PLAYERS_COUNT = 4
PLAYERS_NAMES = ['N', 'E', 'S', 'W']
SIDES_NAMES = ['NS, WE']
PLAYERS_CARDS_COUNT = 13

COLORS_COUNT = 4
COLORS_NAMES = ['S', 'H', 'D', 'C']

CARDS_NAMES = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

ALL_CARDS_COUNT = len(COLORS_NAMES) * len(CARDS_NAMES)

CARDS_IN_COLOR_COUNT = 13
CARDS_PC = [4, 3, 2, 1] + ([0] * 9)
MAX_PC = 40
MAX_PC_PLAYER = 37

BIDS_COLORS = ['c', 'd', 'h', 's', 'nt']
BIDS_COLORS_COUNT = len(BIDS_COLORS)
BIDS_MAX_LEVEL = 7

SPECIAL_BIDS = ['pass', 'dbl', 'rdbl']

COLOR_BIDS_COUNT = BIDS_MAX_LEVEL * len(BIDS_COLORS)
ALL_POSSIBLE_BIDS_COUNT = COLOR_BIDS_COUNT + len(SPECIAL_BIDS)  # =38

COLOR_BIDS = [str(level+1) + color for level in range(BIDS_MAX_LEVEL) for color in BIDS_COLORS]
ALL_BIDS = COLOR_BIDS + SPECIAL_BIDS

CONTRACT_TYPES = ['', 'dbl', 'rdbl']


# ============ calculate contract value - BEGIN =================================

BASE_TRICKS = 6

PENALTY_FIRST_UNDERTRICK = {
    # non vulnerable
    False: {
        '': 50,
        'dbl': 100,
        'rdbl': 200
    },
    # vulnerable
    True: {
        '': 100,
        'dbl': 200,
        'rdbl': 400
    }
}

PENALTY_SECOND_UNDERTRICK = {
    # non vulnerable
    False: {
        '': 50,
        'dbl': 200,
        'rdbl': 400
    },
    # vulnerable
    True: {
        '': 100,
        'dbl': 300,
        'rdbl': 600
    }
}

PENALTY_FOURTH_UNDERTRICK = {
    # non vulnerable
    False: {
        '': 0,
        'dbl': 100,
        'rdbl': 200
    },
    # vulnerable
    True: {
        '': 0,
        'dbl': 0,
        'rdbl': 0
    }
}

PENALTY_FOURTH_FROM = 4

REWARD_FIRST_TRICK = {'c': 20, 'd': 20, 'h': 30, 's': 30, 'nt': 40}

REWARD_NEXT_TRICK = {'c': 20, 'd': 20, 'h': 30, 's': 30, 'nt': 30}

GAME_REQUIRED_POINTS = 100

REWARD_SLAM = {
    # non vulnerable
    False: {
        6: 500,
        7: 1000
    },
    True: {
        6: 750,
        7: 1500
    }
}

REWARD_GAME = {
    # non vulnerable
    False: 300,
    # vulnerable
    True: 500
}

REWARD_NONGAME = 50

REWARD_DBL = {
    '': 0,
    'dbl': 50,
    'rdbl': 100
}

REWARD_OVERTRICKS_DBL = {
    # non vulnerable
    False: {
        'dbl': 100,
        'rdbl': 200
    },
    # vulnerable
    True: {
        'dbl': 200,
        'rdbl': 400
    },
}

# ============ calculate contract value - END =================================
