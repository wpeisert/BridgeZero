from bridgezero.base_actions_provider import BaseActionsProvider
from bridgezero.bridge import Bridge
from bridgezero.state import State


class ActionsProvider(BaseActionsProvider):
    """
    This class is for manipulating actions by agent
    """
    def get_all_actions_count(self):
        Bridge.getAllActionsCount()

    def get_allowed_actions_list(self, state : State):
        raise NotImplementedError("BaseActionsProvider.get_allowed_actions_list not implemented")

    def get_forbidden_actions_list(self, state : State):
        raise NotImplementedError("BaseActionsProvider.get_forbidden_actions_list not implemented")
