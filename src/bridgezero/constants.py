# declare constants

PLAYERS_COUNT = 4
PLAYERS_NAMES = ['N', 'E', 'S', 'W']
SIDES_NAMES = ['NS, WE']
PLAYERS_CARDS_COUNT = 13

COLORS_COUNT = 4;
COLORS_NAMES = ['S', 'H', 'D', 'C']

CARDS_NAMES = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

CARDS_IN_COLOR_COUNT = 13
CARDS_PC = [4, 3, 2, 1] + ([0] * 9)
MAX_PC = 40
MAX_PC_PLAYER = 37

BIDS_COLORS = ['c', 'd', 'h', 's', 'nt']
BIDS_MAX_LEVEL = 7

BID_PASS = 'pass'
BID_DBL = 'dbl'
BID_RDBL = 'rdbl'
BIDS_SPECIAL = [BID_PASS, BID_DBL, BID_RDBL]

ALL_POSSIBLE_BIDS_COUNT = len(BIDS_COLORS) * BIDS_MAX_LEVEL + len(BIDS_SPECIAL) # =38
