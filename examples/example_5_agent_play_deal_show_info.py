# ====== PLAY DEAL, SHOW ALL INFO ==================================================================
from bridgezero import constants
from bridgezero.bridge import Bridge
from bridgezero.deal_generator import DealGenerator
from bridgezero.player.OneStepActorCriticEpisodicAgent_player import OneStepActorCriticEpisodicAgent_player
from bridgezero.player.pass_player import PassPlayer
from bridgezero.player.random_player import RandomPlayer
from bridgezero.player.sometimes_random_player import SometimesRandomPlayer
from bridgezero.table import Table

players = [OneStepActorCriticEpisodicAgent_player(), RandomPlayer(), SometimesRandomPlayer(), PassPlayer()]
table = Table(players)
deal = DealGenerator.get_random_deal()
result = table.play_deal(deal)


print()
for player_name, player in zip(constants.PLAYERS_NAMES, players):
    print("{}: {}".format(player_name, type(player).__name__))
print()
print("Deal: {}".format(deal.get_as_PBN()))
Bridge.print_deal(deal)
print("Dealer: {}".format(deal.dealer))
Bridge.print_bidding(result['bidding'])
print("Contract: {}".format(result['contract'].getHash()))
print("Result NS: {}".format(result['result_ns']))

print("Minimax: {}".format(deal.analysis['minimax_contract_NS']))
print("Minimax value NS: {}".format(deal.analysis['minimax_ev_NS']))

#print(deal.analysis)

for a,b in deal.analysis['tricks_probabilities_NS'].probs.items():
    print("{}: {}".format(a, b))

print()
