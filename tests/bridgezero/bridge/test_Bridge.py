from unittest import TestCase

from bridgezero.bridge.Bridge import *


class TestBridge(TestCase):
    def test_get_players_list(self):
        self.assertEqual(BRIDGE_PLAYERS_LIST, ['N', 'E', 'S', 'W'])
