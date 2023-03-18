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
        all_actions = set(range(self.get_all_actions_count()))
        allowed_actions = set(self.get_allowed_actions_list(state))
        return list(all_actions - allowed_actions)
