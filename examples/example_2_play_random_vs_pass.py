# ====== PLAY RANDOM vs. PASS ==================================
from bridgezero.DealAnalysis.DealAnalyser import DealAnalyser
from bridgezero.deal_generator import DealGenerator
from bridgezero.player.pass_player import PassPlayer
from bridgezero.player.random_player import RandomPlayer
from bridgezero.table import Table

total = 0
count = 0

#players = [SometimesRandomPlayer(0.0), SometimesRandomPlayer(1.0), SometimesRandomPlayer(0.0), SometimesRandomPlayer(1.0)]
#players = [SometimesRandomPlayer(0.5), RandomPlayer(), SometimesRandomPlayer(0.5), RandomPlayer()]
players = [RandomPlayer(),PassPlayer(),RandomPlayer(),PassPlayer()]
table = Table(players)

deals = []

for iter in range(50):
    deal = DealGenerator.get_random_deal()
    DealAnalyser.analyseDeal(deal)
    deals.append(deal)

deals_big = deals * 100

for iter in range(5000):
    result = table.play_deal(deals_big[iter])
    count += 1
    total += result['result_ns']
    print("Deal: {}, avg: {}".format(count, total/count))
