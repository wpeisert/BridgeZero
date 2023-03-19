#!/usr/bin/env python

class BasePlayer:
    """Base class for players
    """
    def player_init(self, cards, we_vulnerable, they_vulnerable):
        """Player gets his cards and vulnerability info
        Here can: initiate RL agent
        """
        raise NotImplementedError()

    def player_bid(self, bidding):
        """Player starts bidding
            Places his bid
        """
        raise NotImplementedError()

    def player_next_bid(self, reward, bidding):
        """Player continues bidding
        Although during bidding no reward exists,
        there may be used EXTERNAL ADVISORY LEARNING
        """
        raise NotImplementedError()

    def player_end_info(self, reward, finished_bidding):
        """Player gets final reward
        Also he can check the final bidding (e.g. to scream on the partner; or, better to learn something)
        """
        raise NotImplementedError()
