#!/usr/bin/env python

"""RL agent
"""
from bridgezero.base_player import BasePlayer
from bridgezero.bridge import Bridge


class PassPlayer(BasePlayer):
    def player_init(self, cards, we_vulnerable, they_vulnerable):
        pass

    def player_start(self, bidding):
        return Bridge.get_bid_by_name("pass")

    def player_step(self, reward, bidding):
        return Bridge.get_bid_by_name("pass")

    def player_end(self, reward, finished_bidding):
        pass
