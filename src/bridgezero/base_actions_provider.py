from bridgezero.state import State


class BaseActionsProvider:
    """
    This class is a base class for manipulating actions by agent
    """
    def get_all_actions_count(self):
        raise NotImplementedError("BaseActionsProvider.get_all_actions_count not implemented")

    def get_allowed_actions_list(self, state : State):
        raise NotImplementedError("BaseActionsProvider.get_allowed_actions_list not implemented")

    def get_forbidden_actions_list(self, state : State):
        raise NotImplementedError("BaseActionsProvider.get_forbidden_actions_list not implemented")
