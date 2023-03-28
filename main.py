"""

Now:

1. It seems that in some circumstances, deal analysis hloops inifinitely
2. We need more tests
3. Main load comes from deal analysis, so it is reasonable to prepare a database of analysed deals and usage of it (many uses of each deal)

But the above points are a bit boring. What is really sexy:

1. Implementation of brain (understood as storing and loading learned weights; maybe together with learning parameters)

What are the players:

1. Player has:
 a) used algorithm (SARSA, Monte Carlo, Actor-Critic, ..)
 b) features functions (currently I have State and StateFeatures classes)
 c) approximation functions for : e.g. linear, quadratic, NN
 d) algorithm learning parameters (alpha_w, alpha_theta, ...

"""
