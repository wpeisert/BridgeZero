from bridgezero.base.base_actions_provider import BaseActionsProvider
from bridgezero.bridge import Bridge
from bridgezero.state import State


class ActionsProvider(BaseActionsProvider):
    """
    This class is for manipulating actions by agent
    """
    def get_all_actions_count(self):
        Bridge.get_all_actions_count()

    def get_allowed_actions_list(self, state : State):
        return Bridge.get_allowed_bids(state.bidding)
