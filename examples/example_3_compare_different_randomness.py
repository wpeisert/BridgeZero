# ====== PLAY DEALS WITH DIFFERENT RANDOMNESS, SHOW RESULT_NS ==================================================================


import numpy as np

from bridgezero.deal_generator import DealGenerator
from bridgezero.player.sometimes_random_player import SometimesRandomPlayer
from bridgezero.table import Table

ROUNDS = 5

print('  ', end='\t')
for rand_EW in np.linspace(0, 1, 6).tolist():
    print(round(rand_EW,1), end='\t')
print('\n')

for rand_NS in np.linspace(0,1,6).tolist():
    print(round(rand_NS,1), end='\t')
    for rand_EW in np.linspace(0,1,6).tolist():

        players = [SometimesRandomPlayer(rand_NS), SometimesRandomPlayer(rand_EW), SometimesRandomPlayer(rand_NS), SometimesRandomPlayer(rand_EW)]
        table = Table(players)
        deals = []
        for i in range(ROUNDS):
            deals.append(DealGenerator.get_random_deal())

        result = table.play_deals(deals)

        print(round(result/ROUNDS), end='\t')

    print('\n')
