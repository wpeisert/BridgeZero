#!/usr/bin/env python
from bridgezero import constants
from bridgezero.base.base_player import BasePlayer
from bridgezero.bridge import Bridge


class PassPlayer(BasePlayer):
    def __init__(self):
        self.bid_pass = Bridge.get_bid_by_name("pass")

    def player_init(self, seat, hand, we_vulnerable, they_vulnerable):
        pass

    def player_bid(self, reward, bidding):
        return self.bid_pass

    def player_end_info(self, reward, finished_bidding):
        pass
