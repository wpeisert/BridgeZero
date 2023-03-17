import numpy as np
from bridgezero import constants

class StateFeatures:
    """
    This class encodes state into features.

    (This is one possible feature assignment. We could also use e.g. NN (RNN for bidding).
    So maybe this should be a class named e.g. SimpleStateFeatures derived from BaseStateFeatures)

    The state consists of:
     - player cards - 13 of 52
     - bidding so far
     - parties vulnerabilities

    Data taken into account:
     - Ns, Nh, Nd, Nc - number of spades, hearts, diamonds, clubs (all of range: 0-13)
     - PC - range 0-37
     - weVuln, theyVuln - 1/0

    Features:
     - tilings for each color: (-colors_tiles_width) - 0, (-colors_tiles_width+1) - 1, ..., 0 - colors_tiles_width, 1 - (colors_tiles_width+1), ..., 13 - (colors_tiles_width+13);
       this gives BINARY features cnt: (14 + colors_tiles_width) features for each color (i. e. x4 colors)
     - tilings for PCs: (-pc_tiles_width) - 0, (-pc_tiles_width+1) - 1, ..., 0-pc_tiles_width, 1-(pc_tiles_width+1), ..., 37 - (pc_tiles_width+37);
       this gives BINARY features cnt: 37 + pc_tiles_width
     - weVuln, theyVuln - 1/0;
       this gives BINARY features cnt: 2

     - bidding: for each player there is a vector of size 1x38 (all bids) having value: 0 - bid didnt appear, 1 - bid was placed, 0+ - for pass, x, xx - count of apperance of pass, dbl, rdbl respectively;
       this gives SMALL INT features cnt: 38 for each player
     - bidding: last three bids: last_bids_count * vector 1x38;
       this gives three 1-HOT features cnt: last_bids_count * 38

    TOTAL features cnt: 4 * (14 + colors_tiles_width) + (38 + pc_tiles_width) + 2 + 4 * 38 + last_bids_count * 38

    Features are sparse. Most of them are binary with exceptions for count of passes, dbls and rdbls bid by a player.
    """

    def __init__(self, colors_tiles_width = 2, pc_tiles_width = 3, last_bids_count = 3):
        """
        :param colors_tiles_width: Width of intervals for player cards of given color
        :param pc_tiles_width: Width of intervals for player PCs
        :param last_bids_count: Count of last bids in feature vector
        """
        self.colors_tiles_width = colors_tiles_width
        self.pc_tiles_width = pc_tiles_width
        self.last_bids_count = last_bids_count

    def get_features(self, cards, bidding, we_vulnerable, they_vulnerable):
        raise NotImplementedError("StateFeatures.get_features not implemented")
        return np.array([0] * 373) # 373 - default number of features

    def get_features_count(self):
        return \
            constants.PLAYERS_COUNT * (constants.CARDS_IN_COLOR_COUNT + 1 + self.colors_tiles_width) + \
            constants.MAX_PC_PLAYER + 1 + self.pc_tiles_width + \
            2 + \
            constants.PLAYERS_COUNT * constants.ALL_POSSIBLE_BIDS_COUNT + \
            constants.ALL_POSSIBLE_BIDS_COUNT * self.last_bids_count
