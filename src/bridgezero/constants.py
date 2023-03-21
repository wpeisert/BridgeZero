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
ALL_POSSIBLE_BIDS_COUNT = COLOR_BIDS_COUNT + len(SPECIAL_BIDS) # =38

COLOR_BIDS = [str(level+1) + color for level in range(BIDS_MAX_LEVEL) for color in BIDS_COLORS]
ALL_BIDS = COLOR_BIDS + SPECIAL_BIDS
