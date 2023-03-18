from bridgezero.state import State

class BaseStateFeatures:
    """
    This class is a base class for encoding state features.
    """
    def get_features(self, state : State):
        raise NotImplementedError("BaseStateFeatures.get_features not implemented")

    def get_features_count(self):
        raise NotImplementedError("BaseStateFeatures.get_features not implemented")
