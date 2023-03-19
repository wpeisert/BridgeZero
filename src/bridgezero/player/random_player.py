#!/usr/bin/env python
import random

from bridgezero.base.base_player import BasePlayer
from bridgezero.bridge import Bridge


class RandomPlayer(BasePlayer):
    def player_init(self, seat, hand, we_vulnerable, they_vulnerable):
        pass

    def player_bid(self, reward, bidding):
        return random.choice(Bridge.get_allowed_bids_list(bidding))

    def player_end_info(self, reward, finished_bidding):
        pass
