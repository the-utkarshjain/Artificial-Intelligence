#!/usr/bin/python3

# Functions in classes representing state space search problems:
#   __init__    To create a state (a starting state for search)
#   __repr__    To construct a string that represents the state
#   __hash__    Hash function for states
#   __eq__      Equality for states
#   successors  Returns [(a1,s1,c1),...,(aN,sN,cN)] where each si is
#               the successor state when action called ai is taken,
#               and ci is the associated cost.
#               Here the name ai of an action is a string.

import time
import queue
import itertools

DEBUG=False
#DEBUG=True
ff = 0

# A*

def ASTAR(initialstate,goaltest,h):
    visited = dict() # dictionary for visited states (OPEN U CLOSED)
    predecessor = dict() # dictionary for predecessors
    g = dict() # dictionary for holding cost-so-far
    f = dict()

    q = queue.PriorityQueue()
    q.put((h(initialstate), initialstate))
    predecessor[initialstate] = None
    g[initialstate] = 0
    f[initialstate] = h(initialstate)
    visited[initialstate] = 1
    goalcost = float("inf")

    while not q.empty():
        x, current = q.get()
        if(x < goalcost):
            for a,state,cost in current.successors():
                new_cost = g[current] + cost
                if (state not in g.keys()):
                    g[state] = new_cost
                    predecessor[state] = current
                    priority = new_cost + h(state)
                    q.put((priority,state))
                    if(goaltest(state)):
                        goalcost = new_cost
    print(goalcost)
    return (predecessor, goalcost)

# ASTAR returns a pair (plan,cost)
# where
#   plan is the sequence of states on an optimal path to goals,
#   cost is the sum of the costs of actions on that path.
