from bridgezero.bridge_bidding_checker import BridgeBiddingChecker

def test_get_bid_by_name():
    assert BridgeBiddingChecker.get_bid_by_name("pass") == 35
    assert BridgeBiddingChecker.get_bid_by_name("dbl") == 36
    assert BridgeBiddingChecker.get_bid_by_name("rdbl") == 37
    assert BridgeBiddingChecker.get_bid_by_name("1c") == 0
    assert BridgeBiddingChecker.get_bid_by_name("7nt") == 34

def test_is_bidding_finished():
    assert True == BridgeBiddingChecker.is_bidding_finished([35,35,35,35])
    assert True == BridgeBiddingChecker.is_bidding_finished([7,35,35,35])
    assert False == BridgeBiddingChecker.is_bidding_finished([35,35,35])
    assert False == BridgeBiddingChecker.is_bidding_finished([35,35,35,2,35,35])

def test_get_allowed_bids_list():
    assert [35, 36] == BridgeBiddingChecker.get_allowed_bids_list([34])
    assert [35, 36] == BridgeBiddingChecker.get_allowed_bids_list([34,35,35])
    assert [35, 37] == BridgeBiddingChecker.get_allowed_bids_list([34,36])
    assert [35, 37, 31, 32, 33, 34] == BridgeBiddingChecker.get_allowed_bids_list([30,36])

