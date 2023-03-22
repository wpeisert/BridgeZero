from bridgezero import constants
from bridgezero.Bidding.BiddingService import BiddingService
from bridgezero.bridge import Bridge


class Table:
    """
    This class:
    1. Gets: 4 players, a batch of deals (later: a generator)
    2. Organizes playing for all players (checking correctness of bidding)
    3. Returns tabular and summary results (and stores them to file)
    """
    def __init__(self, players = None):
        self.players = {} # dictionary: seat -> player obj; e.g. 'N' -> playerObj
        if players is not None:
            self.set_players(players)

    def set_players(self, players):
        for (player_name, player_obj) in zip(constants.PLAYERS_NAMES, players):
            self.players[player_name] = player_obj

    def set_player(self, player_name, player_obj):
        self.players[player_name] = player_obj

    def play_round(self, deals, round_info: str = None):
        self.begin_round(round_info)
        for deal in deals:
            result = self.play_deal(deal)
        self.end_round()
        raise NotImplementedError()

    def play_deal(self, deal):
        """
        Internal method playing single deal
        :param deal: deal
        :return:
        """

        # initiate players
        self.players['N'].player_init('N', deal.get_hand('N'), deal.get_side_ns_vulnerable(), deal.get_side_ew_vulnerable())
        self.players['S'].player_init('S', deal.get_hand('S'), deal.get_side_ns_vulnerable(), deal.get_side_ew_vulnerable())
        self.players['W'].player_init('W', deal.get_hand('W'), deal.get_side_ew_vulnerable(), deal.get_side_ns_vulnerable())
        self.players['E'].player_init('E', deal.get_hand('E'), deal.get_side_ew_vulnerable(), deal.get_side_ns_vulnerable())

        # initiate bidding
        bidding = []
        current_player = deal.get_dealer()

        # run bidding
        while True:
            bid = self.players[current_player].player_bid(0, bidding)
            if bid not in Bridge.get_allowed_bids_list(bidding):
                raise Exception('Player incorrect bid')
            bidding.append(bid)
            if Bridge.is_bidding_finished(bidding):
                break
            current_player = Bridge.get_next_player_name(current_player)

        # bidding finished
        result_ns, contract = BiddingService.calculate_ns_result(deal, bidding)

        self.players['N'].player_end_info(result_ns, bidding)
        self.players['S'].player_end_info(result_ns, bidding)
        self.players['W'].player_end_info(-result_ns, bidding)
        self.players['E'].player_end_info(-result_ns, bidding)

        return {"bidding": bidding, "result_ns": result_ns, "contract": contract}

        # TODO - MORE TO DO: Here save bidding and results info round data

    def begin_round(self, round_info: str = None):
        raise NotImplementedError()

    def end_round(self):
        raise NotImplementedError()
