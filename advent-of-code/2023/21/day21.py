import os
from collections import defaultdict, deque, Counter
import re
import heapq
import math

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/21/input.txt") as f:
    G = f.read().splitlines()


# Part 1
m = len(G)

# Refactored into a function during part 2
def explore(i, j, steps):
    q = deque([])
    tilesByStep = []
    seen = set()
    q.append((i, j))
    for _ in range(steps + 1):
        if len(tilesByStep) > 2 and tilesByStep[-1] == 0 and tilesByStep[-2] == 0:
            break
        newTiles = 0
        for _ in range(len(q)):
            i, j = q.popleft()
            if i < 0 or i >= m or j < 0 or j >= m or (i, j) in seen or G[i][j] == '#':
                continue
            newTiles += 1
            seen.add((i, j))
            q.extend([(i+1, j), (i-1, j), (i, j+1), (i, j-1)])
        tilesByStep.append(newTiles)

    for i in range(len(tilesByStep) - 2):
        tilesByStep[i + 2] += tilesByStep[i]
    
    if steps >= len(tilesByStep):
        return tilesByStep[-1 if len(tilesByStep)%2 != steps%2 else -2]
    return tilesByStep[steps]

    

for i in range(m):
    for j in range(m):
        if G[i][j] == 'S':
            s = (i, j)
    
print(explore(*s, 64))

# Part 2
# Hmm well this is leagues beyond brute force...
# Here's what we're gonna do: 
# 1: Calculate a giant diamond of full explored maps
# 2: Determine the arrangement of all partially explored edge maps
# 3: Calculate those partial explorations
# 4: Sum everything up

totalSteps = 26501365
mapRadius = totalSteps // m # 202300
r = totalSteps % m # 65
# Map is 131x131
# There are clear rows and columns on every edge and middle (direct paths everywhere)

# Map has 7331 even step tiles, 7282 odd step tiles
# 130 steps to explore from S
# 195 from edge midpoint
# 260 steps from corner

res = 0
# fully explored maps
res += mapRadius**2 * explore(*s, 130) + (mapRadius - 1)**2 * explore(*s, 131)
# partially explored maps from an edge's midpoint (corners of the exploration diamond)
res += sum([explore(i, j, 130) for i, j in ((0, m//2), (m-1, m//2), (m//2, 0), (m//2, m-1))])
# lesser explored corners
res += 202300 * sum([explore(i, j, r-1) for i, j in ((0, 0), (0, m-1), (m-1, 0), (m-1, m-1))])
# greater explored corners
res += 202299 * sum([explore(i, j, m+r-1) for i, j in ((0, 0), (0, m-1), (m-1, 0), (m-1, m-1))])

print(res)


