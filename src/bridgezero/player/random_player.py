#!/usr/bin/env python
import random

from bridgezero.base.base_player import BasePlayer
from bridgezero.bridge import Bridge


class RandomPlayer(BasePlayer):
    def player_init(self, cards, we_vulnerable, they_vulnerable):
        pass

    def player_start(self, bidding):
        return self._get_random_move(bidding)

    def player_step(self, reward, bidding):
        return self._get_random_move(bidding)

    def player_end(self, reward, finished_bidding):
        pass


    def _get_random_move(self, bidding):
        return random.choice(Bridge.get_allowed_bids(bidding))