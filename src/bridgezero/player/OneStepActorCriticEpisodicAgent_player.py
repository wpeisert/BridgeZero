#!/usr/bin/env python
from bridgezero.actions_provider import ActionsProvider
from bridgezero.agent.OneStepActorCriticEpisodic_agent import OneStepActorCriticEpisodic_agent
from bridgezero.base.base_player import BasePlayer
from bridgezero.state import State
from bridgezero.state_features import StateFeatures


class OneStepActorCriticEpisodicAgent_player(BasePlayer):
    def __init__(self):
        self.state = None

        self.agent_started = False

        self.agent = OneStepActorCriticEpisodic_agent()
        agent_info = {
            "state_feature_coder": StateFeatures(),
            "actions_provider": ActionsProvider(),

            "actor_step_size": 1e-3,
            "critic_step_size": 1e-2,

            "seed": 99,
        }
        self.agent.agent_init(agent_info)

    def player_init(self, seat, hand, we_vulnerable, they_vulnerable):
        self.state = State(seat=seat, hand=hand, we_vulnerable=we_vulnerable, they_vulnerable=they_vulnerable)
        self.agent_started = False

    def player_bid(self, reward, bidding):
        self.state.set(bidding=bidding)
        if self.agent_started:
            action = self.agent.agent_step(reward, self.state)
        else:
            action = self.agent.agent_start(self.state)
        self.agent_started = True
        return action

    def player_end_info(self, reward, finished_bidding):
        self.agent.agent_end(reward)
