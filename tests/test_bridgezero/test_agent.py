import numpy as np

from bridgezero.agent.ActorCriticContinuing_agent import ActorCriticContinuing_agent
from bridgezero.base.base_actions_provider import BaseActionsProvider
from bridgezero.base.base_state_features import BaseStateFeatures
from bridgezero.state import State


class StateFeaturesTestHelper(BaseStateFeatures):
    FEATURES_CNT = 4

    def __init__(self):
        self.counter = 0

    def get_features_count(self):
        return StateFeaturesTestHelper.FEATURES_CNT

    def get_features(self, state: State):
        self.counter += 1
        features = np.array([self.counter * i for i in range(StateFeaturesTestHelper.FEATURES_CNT)])
        return features


class ActionsProviderTestHelper(BaseActionsProvider):
    def get_all_actions_count(self):
        return 3

    def get_allowed_actions_list(self, state: State):
        return [0, 1, 2]


def get_initiated_agent():
    agent_info = {
        "state_feature_coder": StateFeaturesTestHelper(),
        "actions_provider": ActionsProviderTestHelper(),

        "actor_step_size": 1e-3,
        "critic_step_size": 1e-2,
        "avg_reward_step_size": 1e-2,

        "actions_count": 3,
        "seed": 33
    }

    agent = ActorCriticContinuing_agent()
    agent.agent_init(agent_info)

    return agent


def test_agent_start():
    agent = get_initiated_agent()
    state = State()

    action = agent.agent_start(state)
    assert action == 0
    assert agent.last_features.tolist() == [0, 1, 2, 3]
    action = agent.agent_start(state)
    assert action == 1
    assert agent.last_features.tolist() == [0, 2, 4, 6]


def test_agent_step():

    # agent start
    agent = get_initiated_agent()
    state = State()

    action1 = agent.agent_start(state)
    assert action1 == 0
    assert agent.last_features.tolist() == [0, 1, 2, 3]

    # agent step 1
    reward = 100
    action2 = agent.agent_step(reward, State())
    assert action2 == 0

    assert agent.last_features.tolist() == [0, 2, 4, 6]

    actor_w_expected = np.array(
        [
            np.array([0, 1.0, 2.0, 3.0])/15.0,
            np.array([0, 1.0, 2.0, 3.0])/(-30.0),
            np.array([0, 1.0, 2.0, 3.0])/(-30.0),
        ]
                                )
    assert np.max(np.abs(agent.actor_w - actor_w_expected)) < 0.00000001

    assert agent.critic_w.tolist() == [0, 1, 2, 3]

    assert agent.avg_reward == 1.0

    # agent step 2
    reward = -100
    action3 = agent.agent_step(reward, State())
    assert action3 == 0

    assert agent.last_features.tolist() == [0, 3, 6, 9]

    actor_w_expected = np.array(
        [
            np.array([0, 1.0, 2.0, 3.0]) * 0.0477994,
            np.array([0, 1.0, 2.0, 3.0]) * -0.0238997,
            np.array([0, 1.0, 2.0, 3.0]) * -0.0238997,
        ]
    )
    assert np.max(np.abs(agent.actor_w - actor_w_expected)) < 0.00001

    critic_w_expected = np.array([0.0, -0.74, -1.48, -2.22])
    assert np.max(np.abs(agent.critic_w - critic_w_expected)) < 0.00001

    assert agent.avg_reward == 0.13
