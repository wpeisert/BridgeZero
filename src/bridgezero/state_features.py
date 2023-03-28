import numpy as np
from bridgezero import constants
from bridgezero.base.base_state_features import BaseStateFeatures
from bridgezero.hand import Hand
from bridgezero.state import State


class StateFeatures(BaseStateFeatures):
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

    def __init__(self, **kwargs):
        """
        :param colors_tiles_width: Width of intervals for player cards of given color
        :param pc_tiles_width: Width of intervals for player PCs
        :param last_bids_count: Count of last bids in feature vector
        """
        self.colors_tiles_width = kwargs.get("colors_tiles_width", 2)
        self.pc_tiles_width = kwargs.get("pc_tiles_width", 3)
        self.last_bids_count = kwargs.get("last_bids_count", 3)

        self.state = None
        self.features = None

    def get_features_count(self):
        return \
            constants.COLORS_COUNT * (constants.CARDS_IN_COLOR_COUNT + 1 + self.colors_tiles_width) + \
            constants.MAX_PC_PLAYER + 1 + self.pc_tiles_width + \
            2 + \
            constants.PLAYERS_COUNT * constants.ALL_POSSIBLE_BIDS_COUNT + \
            constants.ALL_POSSIBLE_BIDS_COUNT * self.last_bids_count

    def get_features(self, state : State):
        # raise NotImplementedError("StateFeatures.get_features not implemented")
        # return np.array([0] * 373) # 373 - default number of features
        self.state = state
        self.features = np.zeros(self.get_features_count())
        self._add_colors()
        self._add_pc()
        self._add_vulnerable()

        return self.features

    def _add_colors(self):
        for color in range(constants.COLORS_COUNT):
            self._add_color(color)

    def _add_color(self, color):
        """
        - tilings for each color: (-colors_tiles_width) - 0, (-colors_tiles_width+1) - 1, ..., 0 - colors_tiles_width, 1 - (colors_tiles_width+1), ..., 13 - (colors_tiles_width+13);
        this gives BINARY features cnt: (14 + colors_tiles_width) features for each color (i. e. x4 colors)

        This means that:
        1. There is (constants.CARDS_IN_COLOR_COUNT + 1 + self.colors_tiles_width) fields (tiles) for each color
        2. Each state belongs to (self.colors_tiles_width+1) fields (tiles)
        """
        features_per_color = constants.CARDS_IN_COLOR_COUNT + 1 + self.colors_tiles_width
        interval_start = color * features_per_color + Hand.getColorCardsCount(self.state.hand, color)
        interval_length = self.colors_tiles_width + 1
        for inx in range(interval_start, interval_start + interval_length):
            self.features[inx] = 1

    def _add_pc(self):
        """
        - tilings for PCs: (-pc_tiles_width) - 0, (-pc_tiles_width+1) - 1, ..., 0-pc_tiles_width, 1-(pc_tiles_width+1), ..., 37 - (pc_tiles_width+37);
        this gives BINARY features cnt: 37 + pc_tiles_width
        """
        features_per_color = constants.CARDS_IN_COLOR_COUNT + 1 + self.colors_tiles_width # skip colors (TODO - refactor)
        interval_start = constants.COLORS_COUNT * features_per_color + Hand.getPc(self.state.hand)
        interval_length = self.pc_tiles_width + 1
        for inx in range(interval_start, interval_start + interval_length):
            self.features[inx] = 1

    def _add_vulnerable(self):
        """
        - weVuln, theyVuln - 1/0;
        this gives BINARY features cnt: 2
        """
        features_per_color = constants.CARDS_IN_COLOR_COUNT + 1 + self.colors_tiles_width
        features_for_pc = constants.MAX_PC_PLAYER + self.pc_tiles_width + 1
        vulnerable_start = constants.COLORS_COUNT * features_per_color + features_for_pc # skip colors, PC (TODO - refactor)
        self.features[vulnerable_start] = 1 if self.state.we_vulnerable else 0
        self.features[vulnerable_start + 1] = 1 if self.state.they_vulnerable else 0
