from bridgezero.state_features import StateFeatures

def test1():
    stateFeatures = StateFeatures()
    assert stateFeatures.get_features_count() == 373
