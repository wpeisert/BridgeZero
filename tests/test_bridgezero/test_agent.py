import numpy as np

from bridgezero.agent import ActorCriticSoftmaxEpisodicAgent
from bridgezero.base_state_features import BaseStateFeatures
from bridgezero.state import State


class StateFeaturesHelper(BaseStateFeatures):
    FEATURES_CNT = 4
    COUNTER = 0
    def get_features_count(self):
        return StateFeaturesHelper.FEATURES_CNT
    def get_features(self, state : State):
        StateFeaturesHelper.COUNTER += 1
        features = np.array([StateFeaturesHelper.COUNTER * i for i in range(StateFeaturesHelper.FEATURES_CNT)])
        return features


def test_agent_start():
    agent_info = {
        "state_feature_coder": StateFeaturesHelper(),

        "actor_step_size": 1e-1,
        "critic_step_size": 1e-0,
        "avg_reward_step_size": 1e-2,

        "actions_count": 3,
        "seed": 99
    }

    agent = ActorCriticSoftmaxEpisodicAgent()
    agent.agent_init(agent_info)

    state = State()

    action = agent.agent_start(state)
    assert action == 2
    assert agent.last_features.tolist() == [0, 1, 2, 3]
    action = agent.agent_start(state)
    assert action == 1
    assert agent.last_features.tolist() == [0, 2, 4, 6]

