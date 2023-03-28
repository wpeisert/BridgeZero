import numpy as np

from bridgezero.state import State
from bridgezero.state_features import StateFeatures

def test_number_of_features_default():
    stateFeatures = StateFeatures()
    assert stateFeatures.get_features_count() == 373
    assert stateFeatures.get_features_count() == 16*4 + 41 + 2 + 4*38 + 3*38

def test_number_of_features():
    stateFeatures = StateFeatures(colors_tiles_width=1, pc_tiles_width=1, last_bids_count=1)
    assert stateFeatures.get_features_count() == 15*4 + 39 + 2 + 4*38 + 1*38

def test_empty():
    stateFeatures = StateFeatures()
    state = State(hand=[], bidding=[], we_vulnerable=False, they_vulnerable=False)
    features = stateFeatures.get_features(state)
    assert np.sum(features) == 4 * 3 + 4
    assert features.tolist() == ([1,1,1] + [0]*13) * 4 + [1,1,1,1] + [0]*37 + [0,0] + [0]*4*38 + [0]*3*38

def test_example_hand_colors_pc():
    stateFeatures = StateFeatures()
    state = State(hand=[0,1,2,13,14,15], bidding=[], we_vulnerable=True, they_vulnerable=False)
    #state = State(hand=[5, 6, 7, 17, 18, 19], bidding=[], we_vulnerable=True, they_vulnerable=False)
    features = stateFeatures.get_features(state)
    assert np.sum(features) == 4 * 3 + 4 + 1

    actual = features.tolist()
    expected = ([0,0,0,1,1,1] + [0]*10) * 2 + ([1,1,1] + [0]*13) * 2 + [0]*18 + [1,1,1,1] + [0]*19 + [1,0] + [0]*4*38 + [0]*3*38

    assert actual == expected

def test_vulnerable():
    stateFeatures = StateFeatures()
    for we_vulnerable in [True, False]:
        for they_vulnerable in [True, False]:
            state = State(hand=[5, 6, 7, 17, 18, 19], bidding=[], we_vulnerable=we_vulnerable, they_vulnerable=they_vulnerable)
            features = stateFeatures.get_features(state)

            actual = features.tolist()
            expected = ([0,0,0,1,1,1] + [0]*10) * 2 + ([1,1,1] + [0]*13) * 2 + [1,1,1,1] + [0]*37 +\
                       [1 if we_vulnerable else 0,1 if they_vulnerable else 0] + [0]*4*38 + [0]*3*38

            assert actual == expected

def test_biddings():
    stateFeatures = StateFeatures()
    state = State(hand=[], bidding=[0,35,35,35, 1,36,37,35, 2,36,37,35, 3,35,35,35], we_vulnerable=False, they_vulnerable=False)
    features = stateFeatures.get_features(state)
    assert np.sum(features) == 4 * 3 + 4 + 16 + 3
    assert features.tolist() == ([1,1,1] + [0]*13) * 4 + [1,1,1,1] + [0]*37 + [0,0] + \
            [0]*35 + [4, 0, 0] + \
            [0]*35 + [2, 0, 2] + \
            [0]*35 + [2, 2, 0] + \
            [1,1,1,1] + [0]*34 + \
            ([0]*35 + [1, 0, 0])*3
