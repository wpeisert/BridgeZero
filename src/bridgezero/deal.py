from bridgezero import constants


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
            str += ('' if player_name == 'N' else ' ') + self.get_hand_as_PBN(player_name);

        return str

    def get_hand_as_PBN(self, player_name):

        hand = self.get_hand(player_name)

        cards = {}

        for color_no in range(constants.COLORS_COUNT):
            cards[color_no] = []

        for card_no in hand:
            card_color_no = card_no // constants.CARDS_IN_COLOR_COUNT
            card_in_color_no = card_no % constants.CARDS_IN_COLOR_COUNT
            cards[card_color_no].append(card_in_color_no)

        for color_no in range(constants.COLORS_COUNT):
            cards[color_no].sort()
            cards[color_no][:] = map(lambda card_in_color_no: constants.CARDS_NAMES[card_in_color_no], cards[color_no])
            cards[color_no] = "".join(cards[color_no])

        pbn = ".".join(cards.values())

        return pbn
