import random

from bridgezero import constants
import numpy as np

from bridgezero.deal import Deal


class DealGenerator:
    """
    This class generates deals
    """
    @staticmethod
    def get_random_deal():
        # generate hands
        cards = np.arange(constants.ALL_CARDS_COUNT)
        np.random.shuffle(cards)
        hands = []
        for player_no in range(constants.PLAYERS_COUNT):
            hands.append(cards[player_no * constants.PLAYERS_CARDS_COUNT: (player_no+1) * constants.PLAYERS_CARDS_COUNT - 1])
        # generate other data
        dealer = random.choice(constants.PLAYERS_NAMES)
        side_ns_vulnerable = random.choice([True, False])
        side_we_vulnerable = random.choice([True, False])

        # deal
        deal = Deal(hands, dealer, side_ns_vulnerable, side_we_vulnerable)

        return deal
