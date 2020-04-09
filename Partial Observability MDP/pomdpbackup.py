import numpy as np
# POMDP

states = [0,1]
actions = {"a1","a2"}
observations = {"o1","o2"}

# Dictionary for transition probabilities

P = {
    (0,"a1",0) : 0.2,
    (0,"a1",1) : 0.8,
    (0,"a2",0) : 0.0,
    (0,"a2",1) : 1.0,
    (1,"a1",0) : 0.7,
    (1,"a1",1) : 0.3,
    (1,"a2",0) : 0.6,
    (1,"a2",1) : 0.4
}

# Dictionary for rewards

R = {
    (0,"a1",0) : 1.0,
    (0,"a1",1) : 1.0,
    (0,"a2",0) : 2.0,
    (0,"a2",1) : 2.0,
    (1,"a1",0) : 2.0,
    (1,"a1",1) : 2.0,
    (1,"a2",0) : -1.0,
    (1,"a2",1) : -1.0
}

# Dictionary for observation probabilities

O = {
    ("a1",0,"o1") : 0.0,
    ("a1",0,"o2") : 1.0,
    ("a1",1,"o1") : 0.9,
    ("a1",1,"o2") : 0.1,
    ("a2",0,"o1") : 0.0,
    ("a2",0,"o2") : 1.0,
    ("a2",1,"o1") : 0.9,
    ("a2",1,"o2") : 0.1
}
    
B0 = (0.8,0.2)
gamma=0.9
V0 = [(1.0,2.5),(1.0,0.5)]

# Value of a belief state w.r.t. a value vector

def Bvalue(B,v):
    sum = 0.0
    for s in states:
        sum = sum + B[s]*v[s]
    return sum

# Create value vector based on alpha, a and o

def value(alpha,a,o):
    def stateValue(s):
        sum = 0.0
        for s1 in states:
            sum = sum + P[(s,a,s1)]*(R[(s,a,s1)]+gamma*alpha[s1])
        return O[(a,s,o)]*sum
    return [ stateValue(s) for s in states ]

# Value vector for best policy tree with action a in root
# and immediate subtrees those with value vectors in V

def argmax(lst):
    return max(enumerate(lst), key = lambda x: x[1])[0]

def backupA(a,B,V):
    vsum = [ 0.0 for s in states]
    
    for o in observations:
        val1 = []
        val1.append(value(V[0], a, o))
        val1.append(value(V[1], a, o))


        ba = []
        for v in val1:
            ba.append(Bvalue(B,v))

        for s in states:
            vsum[s] += val1[argmax(ba)][s]

    return vsum

# Value vector for best policy tree that has
# immediate subtrees those with value vectors in V
    
def backup(B,V):
    hasBest = False
    for a in actions:
        alpha = backupA(a,B,V)
        if not hasBest or Bvalue(B,alpha) > bestValue:
            bestValue = Bvalue(B,alpha)
            best = alpha
            hasBest = True
    if not hasBest:
        print("Error")
    return best

# Test case
print("This is a TEST RESULT, which should be [3.98,0.3374]: ")
print(backup(B0,[(0.8,2.2),(1.5,1.5)]))

# Answer to the exercise
print("EXERCISE ANSWER:")
print(backup([0.3,0.7],V0))