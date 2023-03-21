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
Bridge.print_bidding(result['bidding'])
print(result)

pbn = deal.get_as_PBN()
print(pbn)

dd_results = dds.run_dds([deal])
#print(dd_results)
for a,b in dd_results[0].items():
    print("{}: {}".format(a, b))
