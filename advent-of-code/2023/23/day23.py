import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math


cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/23/input.txt") as f:
    grid = f.read().splitlines()


# Part 1
sys.setrecursionlimit(3000)

m = len(grid)

res = 0
def dfs(i, j, seen):
    global res
    if i < 0 or j < 0 or i >= m or j >= m or (i, j) in seen or grid[i][j] == '#':
        return
    seen.add((i, j))
    if grid[i][j] in {'^', '>', 'v', '<'}:
        di, dj = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}[grid[i][j]]
        dfs(i+di, j+dj, seen)
    elif i == m - 1:
        res = max(res, len(seen))
    else:
        for adj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            dfs(*adj, seen)
    seen.discard((i, j))

start = (0, grid[0].index('.'))
dfs(*start, set())

print(res - 1)

# Part 2
# I tried recycling part 1, but it was still computing after running overnight
# To start with, let's build the weighted graph:
# Find all the junctures in the input, which will be the nodes
nodes = [(0, 1)]
for i in range(1, m-1):
    for j in range(1, m-1):
        if grid[i][j] != '#':
            if sum([grid[x][y] != '#' for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1))]) > 2:
                nodes.append((i, j))
nodes.append((m-1, m-2))

# Helper function that returns all weighted edges for a given set of node coordinates
def walkEdges(i, j) -> list[tuple[tuple[int], int]]:
    neighbors = []
    for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
        if grid[x][y] == '#':
            continue
        steps = 1
        prev = (i, j)
        while (x, y) not in nodes:
            for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if (nx, ny) != prev and grid[nx][ny] != '#':
                    prev = (x, y)
                    x, y = nx, ny
                    break
            steps += 1
        neighbors.append(((x, y), steps))
    return neighbors

# Attach nodes to each other
G = defaultdict(list)
for i in range(1, len(nodes) - 1):
    neighbors = walkEdges(*nodes[i])
    for nei, d in neighbors:
        neiId = nodes.index(nei)
        if (neiId, d) not in G[i]:
            G[i].append((neiId, d))
        if (i, d) not in G[neiId]:
            G[neiId].append((i, d))
    
# print(G)

D = defaultdict(int) # D[i] is the longest path from node 0 to node i
seen = set()
# Dfs and backtrack to populate D
def getLongestPath(node, currPath):
    if node in seen:
        return
    seen.add(node)
    D[node] = max(D[node], currPath)
    for adj, dist in G[node]:
        getLongestPath(adj, currPath + dist)
    seen.remove(node)


# Still takes ~16 seconds to compute, but that's a lot better than >8 hours
getLongestPath(0, 0)
print(D[len(G) - 1])
