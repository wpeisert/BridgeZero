#!/usr/bin/env python
import random

from bridgezero.base.base_player import BasePlayer
from bridgezero.player.pass_player import PassPlayer
from bridgezero.player.random_player import RandomPlayer


class SometimesRandomPlayer(BasePlayer):
    """
    Player which acts as a random player with probability given in constructor;
    and acts as pass player with the remaining probability
    """
    def __init__(self, p: float = 0.5):
        self.pass_player = PassPlayer()
        self.random_player = RandomPlayer()
        self.p = min(1, max(0, p))

    def player_init(self, seat, hand, we_vulnerable, they_vulnerable):
        pass

    def player_bid(self, reward, bidding):
        if random.random() > self.p:
            return self.pass_player.player_bid(reward, bidding)
        else:
            return self.random_player.player_bid(reward, bidding)

    def player_end_info(self, reward, finished_bidding):
        pass
