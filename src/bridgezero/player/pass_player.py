#!/usr/bin/env python
from bridgezero import constants
from bridgezero.base.base_player import BasePlayer
from bridgezero.bridge import Bridge


class PassPlayer(BasePlayer):
    def __init__(self):
        self.bid_pass = Bridge.get_bid_by_name(constants.BID_PASS)

    def player_init(self, cards, we_vulnerable, they_vulnerable):
        pass

    def player_start(self, bidding):
        return self.bid_pass

    def player_step(self, reward, bidding):
        return self.bid_pass

    def player_end(self, reward, finished_bidding):
        pass