#!/usr/bin/python3


import time
import queue
import itertools

from MAPP import MAPPGridState, MAPPdistance, MAPPdistance0, createMAPPgrid
from BFS import breadthFirstSearch
from Astar import ASTAR

# ........ ........
# ........ ........
# ........ ..20....
# ........ ..13....
# 21...... ........
# 03...... ........

breadthFirstSearch(MAPPGridState([(0,0),(1,1),(0,1),(1,0)],xsize=5,ysize=5,walls=[]),
                  lambda state: (state.agents == [(3,3),(2,2),(2,3),(3,2)]))

print("CORRECT RESULT: optimal cost is 16.0")
print("RUNTIME ESTIMATE: < 5 seconds")
plan,cost = ASTAR(MAPPGridState([(0,0),(1,1),(0,1),(1,0)],xsize=5,ysize=5,walls=[]),
                  lambda state: (state.agents == [(3,3),(2,2),(2,3),(3,2)]), # goal test
                  MAPPdistance([(3,3),(2,2),(2,3),(3,2)])) # function: distance to goal

for s in plan:
    s.show()


grid0I= ["...........",
         "...........",
         "..12.......",
         "..34.......",
         "...........",
         "...........",
         "..........."]

grid0G= ["...........",
         "...........",
         "...........",
         "...........",
         "...........",
         "........12.",
         "........34"]

print("CORRECT RESULT: optimal cost is 36.0")
print("RUNTIME ESTIMATE: < 15 seconds")
init0,xs0,ys0,w0 = createMAPPgrid(grid0I)
goal0,xs0,ys0,w0 = createMAPPgrid(grid0G)
plan,cost = ASTAR(MAPPGridState(init0,xsize=xs0,ysize=ys0,walls=w0),
                  lambda state: (state.agents == goal0), # goal test
                  MAPPdistance(goal0)) # function: distance to goal
for s in plan:
    s.show()

grid1I= ["...#.........",
         "...#.........",
         "...#.........",
         "...########..",
         "..12......34.",
         "...###..###..",
         "...######....",
         "........#....",
         "........#...."]

grid1G= ["...#.........",
         "...#.........",
         "...#.........",
         "...########..",
         "...34.....21.",
         "...###..###..",
         "...######....",
         "........#....",
         "........#...."]

print("CORRECT RESULT: optimal cost is 36.0")
print("RUNTIME ESTIMATE: < 15 seconds")
init1,xs1,ys1,w1 = createMAPPgrid(grid1I)
goal1,xs1,ys1,w1 = createMAPPgrid(grid1G)
plan,cost = ASTAR(MAPPGridState(init1,xsize=xs1,ysize=ys1,walls=w1),
                  lambda state: (state.agents == goal1), # goal test
                  MAPPdistance(goal1)) # function: distance to goal
for s in plan:
    s.show()

grid2I= ["..1#....",
         "..2#....",
         "........",
         "...#3...",
         "...#4...",
         "...#...."]

grid2G= ["...#1...",
         "...#2...",
         "........",
         "..3#....",
         "..4#....",
         "...#...."]
init2,xs,ys,w = createMAPPgrid(grid1I)
goal2,xs,ys,w = createMAPPgrid(grid1G)

breadthFirstSearch(MAPPGridState([(2,5),(2,4),(4,2),(4,1)],xsize=8,ysize=6,walls=[(3,0),(3,1),(3,2),(3,4),(3,5)]),
           lambda state: (state.agents == [(4,5),(4,4),(2,2),(2,1)]))

print("CORRECT RESULT: optimal cost is 24.0")
print("RUNTIME ESTIMATE: < 3 minutes")
init2,xs2,ys2,w2 = createMAPPgrid(grid2I)
goal2,xs2,ys2,w2 = createMAPPgrid(grid2G)
plan,cost = ASTAR(MAPPGridState(init2,xsize=xs2,ysize=ys2,walls=w2),
                  lambda state: (state.agents == goal2), # goal test
                  MAPPdistance(goal2)) # function: distance to goal
for s in plan:
    s.show()


