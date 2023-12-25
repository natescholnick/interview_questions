import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

file = 'input'
with open(f"{cwd}/advent-of-code/2023/25/{file}.txt") as f:
    lines = f.read().splitlines()


# Part 1
# I don't know much about it, but I think this is a network flow problem
# Selecting a triplet of edges randomly means 3300**3 disconnected checks, too slow
# So we must observe simple paths between nodes, assign flow to edges, and then
# prioritize cutting edges with the highest flow
G = defaultdict(list)
for line in lines:
    nodes = line.split(' ')
    for node in nodes[1:]:
        G[node].append(nodes[0])
        G[nodes[0]].append(node)

print('Graph constructed')

# I am unsure if it will be runtime feasible to compute
# the shortest path for every pair of nodes, but can fall back 
# to using a random sampling. Either way, bfs will be ran many times
nodePaths = {}
nodeDists = {}
def bfs(start):
    dist = []
    parent = {}
    q = deque([])
    visited = set()
    q.append(start)
    visited.add(start)
    while q:
        distGroup = []
        for _ in range(len(q)):
            node = q.popleft()
            distGroup.append(node)
            for adj in G[node]:
                if adj in visited:
                    continue
                visited.add(adj)
                parent[adj] = node
                q.append(adj)
        dist.append(distGroup)
    return parent, dist, len(visited)

def edge(a, b):
    return tuple(sorted([a, b]))

# Compute all shortest paths and trace those paths to compute flow
edgeFlow = defaultdict(int)
count = 1
vertices = len(G)
for node in G:
    print(f'bfs on node #{count} out of {vertices}')
    count += 1
    nodePaths[node], nodeDists[node], _ = bfs(node)
    nodeFlows = defaultdict(lambda: 1)
    for distGroup in nodeDists[node][::-1]:
        if distGroup[0] == node:
            break
        for v in distGroup:
            edgeFlow[edge(v, nodePaths[node][v])] += nodeFlows[v]
            nodeFlows[nodePaths[node][v]] += nodeFlows[v]

edgesToDelete = [x[0] for x in sorted(edgeFlow.items(), reverse=True, key=lambda x: x[1])[:3]]
print(edgesToDelete)
for u, v in edgesToDelete:
    G[u].remove(v)
    G[v].remove(u)

_, __, size1 = bfs(edgesToDelete[0][0])
_, __, size2 = bfs(edgesToDelete[0][1])
print(size1 * size2)

# Nice that only took about a second! The nervous print statements were preemptive haha
# Part 2
# Oh Wastl, you merciful puzzlemaster, you!
# Seeing others do part 2 in 10 seconds on the leaderboard was dazzling me before
# I got here to see all that's left to do is press a button for Christmas to begin :)


        


