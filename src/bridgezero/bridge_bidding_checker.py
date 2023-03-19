#!/usr/bin/env python
from bridgezero import constants


class BridgeBiddingChecker:
    """
    Checks bids
    """
    @staticmethod
    def get_bid_by_name(bid_name: str):
        return constants.ALL_BIDS.index(bid_name)

    @staticmethod
    def is_bidding_finished(bidding):
        if len(bidding) < 4:
            return False
        pass_bid = BridgeBiddingChecker.get_bid_by_name("pass")
        return bidding[-3:].count(pass_bid) == 3 # last three bid are: PASS

    @staticmethod
    def get_allowed_bids_list(bidding):
        if BridgeBiddingChecker.is_bidding_finished(bidding):
            return []

        # pass - always allowed
        pass_bid = BridgeBiddingChecker.get_bid_by_name("pass")
        bids = [pass_bid]

        # dbl
        if BridgeBiddingChecker.is_color_bid(bidding, -1) \
                or BridgeBiddingChecker.is_pass(bidding, -1) \
                and BridgeBiddingChecker.is_pass(bidding, -2) \
                and BridgeBiddingChecker.is_color_bid(bidding, -3):
            bids.append(BridgeBiddingChecker.get_bid_by_name("dbl"))

        # rdbl
        if BridgeBiddingChecker.is_dbl(bidding, -1) \
                or BridgeBiddingChecker.is_pass(bidding, -1) \
                and BridgeBiddingChecker.is_pass(bidding, -2) \
                and BridgeBiddingChecker.is_dbl(bidding, -3):
            bids.append(BridgeBiddingChecker.get_bid_by_name("rdbl"))

        # color bids
        last_color_bid = BridgeBiddingChecker.get_last_color_bid(bidding)
        first_available_color_bid = last_color_bid + 1
        bids = bids + [bid for bid in range(first_available_color_bid, len(constants.COLOR_BIDS))]

        return bids

    # some internal methods

    @staticmethod
    def is_color_bid(bidding, inx):
        if not BridgeBiddingChecker.is_valid_inx(bidding, inx):
            return False
        return bidding[inx] < len(constants.COLOR_BIDS)

    @staticmethod
    def is_pass(bidding, inx):
        if not BridgeBiddingChecker.is_valid_inx(bidding, inx):
            return False
        return bidding[inx] == BridgeBiddingChecker.get_bid_by_name("pass")

    @staticmethod
    def is_dbl(bidding, inx):
        if not BridgeBiddingChecker.is_valid_inx(bidding, inx):
            return False
        return bidding[inx] == BridgeBiddingChecker.get_bid_by_name("dbl")

    @staticmethod
    def get_last_color_bid(bidding):
        inx = -1
        while True:
            if not BridgeBiddingChecker.is_valid_inx(bidding, inx):
                return -1 # not found
            if BridgeBiddingChecker.is_color_bid(bidding, inx):
                return bidding[inx]
            inx -= 1

    @staticmethod
    def is_valid_inx(bidding, inx):
        length = len(bidding)
        return -length <= inx < length
