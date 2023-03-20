from bridgezero import constants


class Hand:
    """
    This class holds single hand cards (all 13 items)
    """
    @staticmethod
    def hand_to_PBN(hand):

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


    @staticmethod
    def PBN_to_hand(pbn):
        hand = []
        cards = pbn.split(".")
        for color_no in range(constants.COLORS_COUNT):
            length = len(cards[color_no])
            for pos in range(length):
                card = cards[color_no][pos]
                hand.append(color_no * constants.CARDS_IN_COLOR_COUNT + constants.CARDS_NAMES.index(card))

        return hand
