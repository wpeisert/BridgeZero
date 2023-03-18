#!/usr/bin/env python

"""RL agent
"""

import numpy as np
import scipy

from bridgezero.base_agent import BaseAgent
from bridgezero.base_state_features import BaseStateFeatures
from bridgezero.state import State


class ActorCriticSoftmaxEpisodicAgent(BaseAgent):
    def __init__(self):
        self.rand_generator = None

        self.actor_step_size = None
        self.critic_step_size = None
        self.avg_reward_step_size = None

        self.state_feature_coder: BaseStateFeatures = BaseStateFeatures()

        self.avg_reward = None
        self.critic_w = None
        self.actor_w = None

        self.actions = None

        self.softmax_prob = None
        self.last_features = None
        self.last_action = None
        self.current_features = None
        self.current_action = None

    def agent_init(self, agent_info=None):
        """Setup for the agent called when the experiment first starts.

        Set parameters needed to setup the semi-gradient TD(0) state aggregation agent.

        Assume agent_info dict contains:
        {
            "state_feature_coder" : BaseStateFeatures

            "discount" : float  # currently not used

            "actor_step_size": float,
            "critic_step_size": float,
            "avg_reward_step_size": float,

            "actions_count": int,
            "seed": int
        }
        """

        # set random seed for each run
        if agent_info is None:
            agent_info = {}
        self.rand_generator = np.random.RandomState(agent_info.get("seed"))

        # set state feature coder
        self.state_feature_coder = agent_info.get("state_feature_coder")

        # set step-size accordingly
        self.actor_step_size = agent_info.get("actor_step_size")
        self.critic_step_size = agent_info.get("critic_step_size")
        self.avg_reward_step_size = agent_info.get("avg_reward_step_size")

        self.actions = list(range(agent_info.get("actions_count")))

        # Set initial values of average reward, actor weights, and critic weights
        self.avg_reward = 0.0
        features_count = self.state_feature_coder.get_features_count()
        self.actor_w = np.zeros((len(self.actions), features_count))
        self.critic_w = np.zeros(features_count)

        self.softmax_prob = None
        self.last_features = None
        self.last_action = None
        self.current_features = None
        self.current_action = None

    def agent_policy(self, state_features):
        """ policy of the agent
        Args:
            state of class State: the state from the environment

        Returns:
            The action selected according to the policy
        """

        # compute softmax probability
        softmax_prob = scipy.special.softmax(
            np.matmul(
                self.actor_w,
                state_features
            )
        )

        # Sample action from the softmax probability array
        # self.rand_generator.choice() selects an element from the array with the specified probability
        chosen_action = self.rand_generator.choice(self.actions, p=softmax_prob)

        # save softmax_prob as it will be useful later when updating the Actor
        self.softmax_prob = softmax_prob

        return chosen_action

    def state_value_function(self, state_features):
        """ state value function
        Args:
            state of class State: the state from the environment

        Returns:
            state value
        """

        state_value = np.matmul(self.critic_w, state_features)

        return state_value

    def agent_start(self, state: State):
        """The first method called when the experiment starts, called after
        the environment starts.
        Args:
            state of class State: the state from the environment's env_start function.
        Returns:
            The first action the agent takes.
        """
        self.current_features = self.state_feature_coder.get_features(state)
        self.current_action = self.agent_policy(self.current_features)

        self.last_action = self.current_action
        self.last_features = np.copy(self.current_features)

        return self.last_action

    def agent_step(self, reward: float, state: State):
        """A step taken by the agent.
        Args:
            reward (float): the reward received for taking the last action taken
            state of class State: the state from the environment's env_step function based on
                                where the agent ended up after the last step.
        Returns:
            The action the agent is taking.
        """

        self.current_features = self.state_feature_coder.get_features(state)

        self.calculate_policy_after_step(reward)

        self.current_action = self.agent_policy(self.current_features)
        self.last_features = self.current_features
        self.last_action = self.current_action

        return self.last_action


    def agent_end(self, reward: float):
        """A step taken by the agent.
        Args:
            reward (float): the reward received for taking the last action taken
            state of class State: the state from the environment's env_step function based on
                                where the agent ended up after the last step.
        Returns:
            The action the agent is taking.
        """

        self.calculate_policy_after_step(reward, True)

        return self.last_action


    def calculate_policy_after_step(self, reward: float, is_terminal: bool = False):
        delta = reward - self.avg_reward + \
                (0 if is_terminal else self.state_value_function(self.current_features)) - \
                self.state_value_function(self.last_features)
        self.avg_reward += self.avg_reward_step_size * delta
        self.critic_w += self.last_features * self.critic_step_size * delta
        for a in self.actions:
            if a == self.last_action:
                self.actor_w[a][self.last_features] += self.actor_step_size * delta * (1 - self.softmax_prob[a])
            else:
                self.actor_w[a][self.last_features] += self.actor_step_size * delta * (0 - self.softmax_prob[a])


    def agent_message(self, message):
        if message == 'get avg reward':
            return self.avg_reward
