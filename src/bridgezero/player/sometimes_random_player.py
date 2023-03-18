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

    def player_init(self, cards, we_vulnerable, they_vulnerable):
        pass

    def player_start(self, bidding):
        return self._get_move(bidding)

    def player_step(self, reward, bidding):
        return self._get_move(bidding)

    def player_end(self, reward, finished_bidding):
        pass

    def _get_move(self, bidding):
        if random.random() < self.p:
            return self.pass_player.player_start(bidding)
        else:
            return self.random_player.player_start(bidding)
