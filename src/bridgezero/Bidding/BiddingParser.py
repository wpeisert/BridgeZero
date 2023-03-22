from bridgezero import constants
from bridgezero.Contract.Contract import Contract
from bridgezero.bridge import Bridge
from bridgezero.bridge_bidding_checker import BridgeBiddingChecker


class BiddingParser:
    @staticmethod
    def getContractWithoutVulnerability(deal, bidding):
        lastColorBid = BridgeBiddingChecker.get_last_color_bid(bidding)
        if -1 == lastColorBid:
            return Contract.PASS()

        lastColorBidIndex = bidding.index(lastColorBid)
        firstColorBid = BridgeBiddingChecker.getFirstColorBidInPairForBid(bidding, lastColorBid)
        firstColorBidIndex = bidding.index(firstColorBid)

        declarer = Bridge.get_next_player_name(deal.dealer, firstColorBidIndex)
        bidColor = lastColorBid % constants.BIDS_COLORS_COUNT
        level = lastColorBid // constants.BIDS_COLORS_COUNT + 1
        type = ''
        bids = bidding[lastColorBidIndex:]
        bid_dbl = Bridge.get_bid_by_name("dbl")
        bid_rdbl = Bridge.get_bid_by_name("rdbl")
        if bid_rdbl in bids:
            type = 'rdbl'
        elif bid_dbl in bids:
            type = 'dbl'

        return Contract(declarer=declarer, bidColor=bidColor, level=level, type=type)
