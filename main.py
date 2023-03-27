"""

Now:

1. It seems that in some circumstances, deal analysis hloops inifinitely
2. We need more tests
3. Main load comes from deal analysis, so it is reasonable to prepare a database of analysed deals and usage of it (many uses of each deal)

But the above points are a bit boring. What is really sexy:

1. Implementation of brain (understood as storing and loading learned weights; maybe together with learning parameters)

What are the players:

1. Player has:
 a) used algorithm (SARSA, Monte Carlo, Actor-Critic, ..)
 b) features functions (currently I have State and StateFeatures classes)
 c) approximation functions for : e.g. linear, quadratic, NN
 d) algorithm learning parameters (alpha_w, alpha_theta, ...

"""

# ====== PLAY DEAL, SHOW ALL INFO ==================================================================
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
