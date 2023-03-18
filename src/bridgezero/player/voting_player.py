#!/usr/bin/env python
import random

from bridgezero.base.base_player import BasePlayer


class VotingPlayer(BasePlayer):
    """
    Player gets a list of players and the probabilities.
    Uses all players (so they can do their stuff), but decides randomly due to given probability weights
    """
    def __init__(self, players_classes, p = None):
        self.players = []
        self.results = []
        for player_class in players_classes:
            self.players.append(player_class())
        self.p = p

    def player_init(self, cards, we_vulnerable, they_vulnerable):
        for player in self.players:
            player.player_init(cards, we_vulnerable, they_vulnerable)

    def player_start(self, bidding):
        self.results = []
        for player in self.players:
            self.results.append(player.player_start(bidding))
        return self._get_result()

    def player_step(self, reward, bidding):
        self.results = []
        for player in self.players:
            self.results.append(player.player_step(reward, bidding))
        return self._get_result()

    def player_end(self, reward, finished_bidding):
        for player in self.players:
            self.results.append(player.player_step(reward, finished_bidding))

    def _get_result(self):
        return random.choices(self.results, weights = self.p)
