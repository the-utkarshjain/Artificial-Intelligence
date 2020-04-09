#!/usr/bin/python3

# Knights, Knaves, and Spies
#
# We consider a variant of the Knights and Knaves puzzles
# with also a third category of persons, Spies.
# The specific properties of these person categories are that
#   - Knights always tells the truth
#   - Knaves always lie
#   - Spies can either tell the truth or lie
#
# An instance of the puzzles consists of indicating what
# the given persons say, and then the task is to figure
# out who is telling the truth and who is lying:
#   You meet three persons. Call them A, B, C.
#   You know that one is a Knight, one is a Knave, and one is a Spy.
#   Each of them makes a statement. First A, then B, and last C.
#   Which one is which?

from logic2 import ATOM, AND, OR, NOT, IMPL
import DPLL2

######### Cardinality constraints #########

def atLeast1(fmas):
  return OR(fmas)

def allpairs(lst): # Helper function for atMost1
  return [ (lst[i],lst[j]) for i in range(0,len(lst)) for j in range(i+1,len(lst)) ]

def atMost1(fmas): 
  return AND([NOT(AND([f1,f2])) for (f1,f2) in allpairs(fmas)])

def exactly1(fmas):
  return AND([atMost1(fmas), atLeast1(fmas)])

people = ("A","B","C")
roles = ("Knight", "Knave", "Spy")
def isa(p,r):
    "Define an atom stating '<person> is a <role>'"
    return ATOM("{0} is a {1}".format(p,r))
def claim(p):
    "Define an atom stating that a person speaks the truth."
    return ATOM("{0}'s statement holds".format(p))

statement = {}

# Test 1
statement["A"] = isa("A","Knight") # I am a knight
statement["B"] = claim("A") # That is correct
statement["C"] = isa("C","Spy") # I am a spy

# Test 2
# statement["A"] = isa("A","Spy") # I am the spy.
# statement["B"] = claim("A") # That is correct.
# statement["C"] = NOT(isa("C","Spy")) # I am not a spy.

# Build formula from given statements
def makeFormulas(statement):
  constraints = []
  # Roles are mutually exclusive
  constraints.append(AND([exactly1([isa(p,r) for r in roles]) for p in people]))
  # And only one role per person
  constraints.append(AND([exactly1([isa(p,r) for p in people]) for r in roles]))
  for p in people:
    # A person is either speaking the truth and is a knight or a spy. Their statement is true.
    # Or, the person is lying and is a knave or a spy. Their statement is false.

    utk1 = AND([statement[p], OR([isa(p, "Knight"), isa(p, "Spy")])])
    utk2 = AND([NOT(statement[p]), OR([isa(p, "Knave"), isa(p, "Spy")])])
    constraints.append( OR([NOT(claim(p)), utk1]) )
    constraints.append( OR([claim(p), utk2]) )

  return AND(constraints)

#for c in constraints:
#  print(c)

sol = DPLL2.SAT(makeFormulas(statement))
# print(sol)

# Show True atoms in valuation
for p in people:
  def truthlies(t):
    if t:
      return "tells the truth"
    else:
      return "lies"
  for r in roles:
    if sol[str(isa(p,r))]:
      print("{0} and {1}".format(isa(p,r),truthlies(sol[str(claim(p))])))
