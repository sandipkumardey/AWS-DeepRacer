# AWS-DeepRacer

## Applying reinforcement learning to AWS DeepRacer

A policy defines the action that the agent should take for a given state. This could conceptually be represented as a table - given a particular state, perform this action.

- **A deterministic policy,** where there is a direct relationship between state and action. This is often used when the agent has a full understanding of the environment and, given a state, always performs the same action.
- In a **stochastic policy,** you have a range of possible actions for a state, each with a probability of being selected. When the policy is queried to return an action for a state it selects one of these actions based on the probability distribution.

This would obviously be a much better policy option for our rock, paper, scissors game as our opponents will no longer know exactly which action we will choose each time we play.

A **Value function,** think of this as looking ahead into the future and figuring out how much reward you expect to get given your current policy.

Say the DeepRacer car (agent) is approaching a corner. The algorithm queries the policy about what to do, and it says to accelerate hard. The algorithm then asks the value function how good it thinks that decision was - but unfortunately, the results are not too good, as it’s likely the agent will go off-track in the future due to his hard acceleration into a corner. As a result, the value is low and the probabilities of that action can be adjusted to discourage the selection of the action and getting into this state.

### Training Algorithms-

The first thing to point out is that AWS DeepRacer uses both PPO and SAC algorithms to train stochastic policies. So they are similar in that regard.

- **PPO** uses **“on-policy” learning**. This means it learns only from observations made by the current policy exploring the environment - using the most recent and relevant data. Say you are learning to drive a car, on-policy learning would be analogous to you reviewing a video of your most recent lesson and taking note of what you did well, and what needs improvement.
- In contrast, **SAC** uses **“off-policy” learning.** This means it can use observations made from previous policies and exploration of the environment - so it can also use old data.

"There is no right or wrong answer. SAC and PPO are two algorithms from a field that is constantly evolving and growing. Both have their benefits and either one could work best depending on the circumstance."

### Reward Functions-

In order to calculate an appropriate reward you need information about the state of the agent and perhaps even the environment. These are provided to you by the AWS DeepRacer system in the form of **input parameters** - in other words, they are parameters for input into your reward function.

There are over 20 parameters available for use, and the reward function is simply a piece of code that uses the input parameters to do some calculations and then output a number, which is the reward.

- The reward function is written in Python as a standard function, but it must be called *reward_function* with a single parameter - which is a Python dictionary containing all the input parameters provided by the AWS DeepRacer system.
