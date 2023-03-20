from bridgezero import constants
from bridgezero.hand import Hand


class Deal:
    """
    This class holds deal data
    """

    def __init__(self, hands = None, dealer = None, side_ns_vulnerable: bool = None, side_ew_vulnerable: bool = None):
        self.hands = {}
        if hands is not None:
            self.set_hands(hands) # dictionary: seat -> hand; e.g. 'N' -> cards on hand
        self.dealer = dealer # one of constants.PLAYERS_NAMES
        self.side_ns_vulnerable = side_ns_vulnerable
        self.side_ew_vulnerable = side_ew_vulnerable

    # setters

    def set_hands(self, hands):
        for (player_name, hand) in zip(constants.PLAYERS_NAMES, hands):
            self.hands[player_name] = hand

    def set_hand(self, player_name, hand):
        self.hands[player_name] = hand

    def set_dealer(self, dealer):
        self.dealer = dealer

    def set_side_ns_vulnerable(self, side_ns_vulnerable: bool):
        self.side_ns_vulnerable = side_ns_vulnerable

    def set_side_ew_vulnerable(self, side_ew_vulnerable: bool):
        self.side_ew_vulnerable = side_ew_vulnerable

    # getters

    def get_hand(self, player_name):
        return self.hands[player_name]

    def get_dealer(self):
        return self.dealer

    def get_side_ns_vulnerable(self):
        return self.side_ns_vulnerable

    def get_side_ew_vulnerable(self):
        return self.side_ew_vulnerable

    # tools

    def get_as_PBN(self):
        str = 'N:'
        for player_name in constants.PLAYERS_NAMES:
            str += ('' if player_name == 'N' else ' ') + Hand.hand_to_PBN(self.get_hand(player_name))

        return str
