#!/usr/bin/env python
from bridgezero import constants
from bridgezero.bridge_bidding_checker import BridgeBiddingChecker


class Bridge:
    """
    Class provides all bridge functionalities
    """
    @staticmethod
    def get_random_initial_state():
        raise NotImplementedError()

    @staticmethod
    def get_all_actions_count():
        return constants.ALL_POSSIBLE_BIDS_COUNT

    @staticmethod
    def get_bid_by_name(bid_name: str):
        return constants.ALL_BIDS.index(bid_name)

    @staticmethod
    def get_allowed_bids_list(bidding):
        return BridgeBiddingChecker.get_allowed_bids_list(bidding)

    @staticmethod
    def is_bidding_finished(bidding):
        return BridgeBiddingChecker.is_bidding_finished(bidding)

    @staticmethod
    def print_bidding(bidding):
        print('')
        for i, bid in enumerate(bidding):
            print(constants.ALL_BIDS[bid], end=('\n' if i%4==3 else '\t'))
        # TODO improve
        print('')
        print('')

    @staticmethod
    def get_next_player_name(player_name, step = 1):
        return constants.PLAYERS_NAMES[ (constants.PLAYERS_NAMES.index(player_name) + step) % constants.PLAYERS_COUNT ]
