# Now comments in Polish - just to free my mind......

"""
Teraz chcemy uzyskac konkretne scenariusze:

1. Siadają czterej gracze do gry i grają określoną liczbę rozdań. Widzę rezultat (IMP)

2. Mogę zdefiniować konkretnych graczy (nazwijmy ich: gracze nazwani - named players);
chodzi o to, by ten konkretny gracz mógł sobie zapisywać i wczytywać mózg

3. Koncepcja: mózg gracza

Ma to wyglądać tak:

Stała definicja:
players = [
    {
        name: 'Wojtek',
        class: 'RLagent',
        init_info: {
            actor_step_size: 0.01
        }
    },
    {
        name: 'Passer',
        class: PassPlayer,
        brain: False,
    },
    {
        name: 'Totally crazy',
        class: PassPlayer
    },

]
"""
from bridgezero.bridge import Bridge
from bridgezero.deal_generator import DealGenerator
from bridgezero.player.pass_player import PassPlayer
from bridgezero.player.random_player import RandomPlayer
from bridgezero.player.sometimes_random_player import SometimesRandomPlayer
from bridgezero.table import Table
import bridgezero.dds as dds

players = [SometimesRandomPlayer(), PassPlayer(), RandomPlayer(), SometimesRandomPlayer(0.3)]
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
