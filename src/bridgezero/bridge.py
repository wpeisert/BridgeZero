#!/usr/bin/env python
from bridgezero import constants
from bridgezero.bridge_bidding_checker import BridgeBiddingChecker
from bridgezero.hand import Hand


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
    def get_next_player_name(player_name, step = 1):
        return constants.PLAYERS_NAMES[ (constants.PLAYERS_NAMES.index(player_name) + step) % constants.PLAYERS_COUNT ]

    @staticmethod
    def print_bidding(bidding):
        print('')
        for i, bid in enumerate(bidding):
            print(constants.ALL_BIDS[bid], end=('\n' if i%4==3 else '\t'))
        # TODO improve
        print('')
        print('')

    @staticmethod
    def print_deal(deal):
        lines = {}
        for player_name in constants.PLAYERS_NAMES:
            lines[player_name] = Bridge._get_print_hand(Hand.hand_to_PBN(deal.get_hand(player_name)))
        max_len_W = max([len(x) for x in lines['W']])
        INDENT = 10
        indent_by_W = max(10, INDENT - 3)
        print('')

        for line in lines['N']:
            print(' ' * indent_by_W + line)
        for line1, line2 in zip (lines['W'], lines['E']):
            print(line1 + ' ' * (INDENT + indent_by_W - len(line1)) + line2)
        for line in lines['S']:
            print(' ' * indent_by_W + line)

        print('')
        print('')

    @staticmethod
    def _get_print_hand(hand: str):
        lines = []
        for symbol, cards in zip(constants.COLORS_PRINT_SYMBOLS, hand.split(".")):
            lines.append(symbol + ' ' + cards)
        return lines