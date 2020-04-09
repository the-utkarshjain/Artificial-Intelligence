
import random

from qlearnexamples import *

# The Q-Learning Algorithm

# Implementing the Q-learning algorithm for MDPs.
#   The Q-values are represented as a Python dictionary Q[s,a],
# which is a mapping from the state indices s=0..stateMax to
# and actions a to the Q-values.
#
# Choice of actions are completely random

# bestActionFor chooses the best action for 'state', given Q values

def bestActionFor(mdp,state,Q):
  actions = mdp.applicableActions(state)
  if actions == []:
    return -1
  else:
    value = [Q[state,a] for a in actions]
    action = actions[value.index(max(value))]
    return action

# valueOfBestAction gives the value of best action for 'state'

def valueOfBestAction(mdp,state,Q):
  value = bestActionFor(mdp, state, Q)
  if value == -1:
    return 0
  else:  
    return Q[state, value]

# 'execute' randomly chooses a successor state for state s w.r.t. action a.
# The probability with which is given successor is chosen must respect
# to the probability given by mdp.successors(s,a).
# It returns a tuple (s2,r), where s2 is the successor state and r is
# the reward that was obtained.

def execute(mdp,s,a):
  succ = mdp.successors(s, a)
  state = [p[0] for p in succ]
  prob = [p[1] for p in succ]
  reward = [p[2] for p in succ]

  choice = random.choices(state,prob)[0]
  # print(reward, choice, state.index(choice[0]))
  rchoice = reward[state.index(choice)]
  
  return (choice, rchoice)

# Qlearning returns the Q-value function after performing the given
#   number of iterations i.e. Q-value updates.

def Qlearning(mdp,gamma,lambd,iterations):
  # The Q-values are a real-valued dictionary Q[s,a] where s is a state and a is an action.
  state =  0 # Always start from state 0
  Q = dict()
  for s in range(mdp.stateMax + 1):
    for a in mdp.applicableActions(s):
      Q[s,a] = 0

  for i in range(iterations):
    action = random.choice(mdp.applicableActions(s))
    nextstate = execute(mdp, state, action)
    Q[state, action] = (1 - lambd)*Q[state, action] + lambd*(nextstate[1] + gamma*valueOfBestAction(mdp, nextstate[0], Q))
    state = nextstate[0]
  return Q

# makePolicy constructs a policy, i.e. a mapping from state to actions,
#   given a Q-value function as produced by Qlearning.

def makePolicy(mdp,Q):
  # A policy is an action-valued dictionary P[s] where s is a state
  P = dict()
  for s in range(mdp.stateMax + 1):
    P[s] = bestActionFor(mdp, s, Q)
  return P

# makeValues constructs the value function, i.e. a mapping from states to values,
#   given a Q-value function as produced by Qlearning.

def makeValues(mdp,Q):
  # A value function is a real-valued dictionary V[s] where s is a state
  V = dict()

  for s in range(mdp.stateMax + 1):
    V[s] = valueOfBestAction(mdp, s, Q)
  
  return V
