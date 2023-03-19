#!/usr/bin/env python
import random

from bridgezero.base.base_player import BasePlayer
from bridgezero.bridge import Bridge


class RandomPlayer(BasePlayer):
    def player_init(self, cards, we_vulnerable, they_vulnerable):
        pass

    def player_bid(self, bidding):
        return self._get_random_move(bidding)

    def player_next_bid(self, reward, bidding):
        return self._get_random_move(bidding)

    def player_end_info(self, reward, finished_bidding):
        pass


    def _get_random_move(self, bidding):
        return random.choice(Bridge.get_allowed_bids(bidding))