#!/usr/bin/env python

class BasePlayer:
    """Base class for players
    """
    def player_init(self, seat, hand, we_vulnerable, they_vulnerable):
        """Player gets his hand and vulnerability info
        Here can: initiate RL agent
        """
        raise NotImplementedError()

    def player_bid(self, reward, bidding):
        """Player places his bid
        Returns: bid
        """
        raise NotImplementedError()

    def player_end_info(self, reward, finished_bidding):
        """Player gets final reward
        Also he can check the final bidding (e.g. to scream on the partner; or, better to learn something)
        """
        raise NotImplementedError()
