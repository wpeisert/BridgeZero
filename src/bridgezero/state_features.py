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

        self.feature_counts = {
            'colors': constants.COLORS_COUNT * (constants.CARDS_IN_COLOR_COUNT + 1 + self.colors_tiles_width),
            'pc': constants.MAX_PC_PLAYER + 1 + self.pc_tiles_width,
            'vulnerable': 2,
            'bidding': constants.PLAYERS_COUNT * constants.ALL_POSSIBLE_BIDS_COUNT,
            'last_bids': constants.ALL_POSSIBLE_BIDS_COUNT * self.last_bids_count
        }

    def get_features_count(self):
        return \
            self.feature_counts['colors'] + \
            self.feature_counts['pc'] + \
            self.feature_counts['vulnerable'] + \
            self.feature_counts['bidding'] + \
            self.feature_counts['last_bids']

    def get_features(self, state : State):
        # raise NotImplementedError("StateFeatures.get_features not implemented")
        # return np.array([0] * 373) # 373 - default number of features
        self.state = state
        self.features = np.zeros(self.get_features_count())
        self._add_colors()
        self._add_pc()
        self._add_vulnerable()
        self._add_biddings()
        self._add_last_bids()

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
        interval_start = self.feature_counts['colors'] + Hand.getPc(self.state.hand)
        interval_length = self.pc_tiles_width + 1
        for inx in range(interval_start, interval_start + interval_length):
            self.features[inx] = 1

    def _add_vulnerable(self):
        """
        - weVuln, theyVuln - 1/0;
        this gives BINARY features cnt: 2
        """
        vulnerable_start = self.feature_counts['colors'] + self.feature_counts['pc']
        self.features[vulnerable_start] = 1 if self.state.we_vulnerable else 0
        self.features[vulnerable_start + 1] = 1 if self.state.they_vulnerable else 0

    def _add_biddings(self):
        for player_no in range(constants.PLAYERS_COUNT):
            self._add_player_bidding(player_no)

    def _add_player_bidding(self, player_no):
        """
        - bidding: for each player there is a vector of size 1x38 (all bids) having value: 0 - bid didnt appear, 1 - bid was placed, 0+ - for pass, x, xx - count of apperance of pass, dbl, rdbl respectively;
        this gives SMALL INT features cnt: 38 for each player
        """
        offset = self.feature_counts['colors'] + self.feature_counts['pc'] + self.feature_counts['vulnerable'] + player_no * constants.ALL_POSSIBLE_BIDS_COUNT
        inx = player_no
        while len(self.state.bidding) > inx:
            value = self.state.bidding[-inx - 1]
            self.features[offset + value] += 1
            inx += constants.PLAYERS_COUNT

    def _add_last_bids(self):
        offset = self.feature_counts['colors'] + self.feature_counts['pc'] + self.feature_counts['vulnerable'] + self.feature_counts['bidding']
        for item in range(self.last_bids_count):
            if item >= len(self.state.bidding):
                break
            value = self.state.bidding[-item - 1]
            self.features[offset + value] += 1
            offset += constants.ALL_POSSIBLE_BIDS_COUNT
