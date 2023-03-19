#!/usr/bin/env python
from bridgezero import constants
from bridgezero.state import State


class Bridge:
    """
    Class provides all bridge functionalities
    """
    def get_random_initial_state():
        raise NotImplementedError()

    def getAllowedActions(state : State):
        raise NotImplementedError()

    def get_all_actions_count():
        return constants.ALL_POSSIBLE_BIDS_COUNT

    def get_bid_by_name(bid_name: str):
        """
        :return: bid index (action number)
        """
        raise NotImplementedError()

    def get_allowed_bids_list(bidding):
        raise NotImplementedError()

    def get_next_player_name(player_name):
        return constants.PLAYERS_NAMES[ (constants.PLAYERS_NAMES.index(player_name) + 1) % constants.PLAYERS_COUNT ]