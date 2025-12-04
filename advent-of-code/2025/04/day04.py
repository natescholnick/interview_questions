
import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2025/04/input.txt") as f:
    lines = f.read().splitlines()

G = [[c for c in line] for line in lines]
    
# Part 1
m = len(G)
def adjacent(i, j):
    adj = []
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            ni, nj = i + di, j + dj
            if (i == ni and j == nj) or ni < 0 or nj < 0 or ni == m or nj == m:
                continue
            if G[ni][nj] == '@':
                adj.append((ni, nj))
    return adj

res = 0
for i in range(m):
    for j in range(m):
        if G[i][j] == '@' and len(adjacent(i, j)) < 4:
            res += 1

print(res)

# Part 2
res2 = 0
to_consider = []
for i in range(m):
    for j in range(m):
        if G[i][j] == '@':
            to_consider.append((i, j))

while to_consider:
    added = set()
    next_round = []
    for i, j in to_consider:
        if G[i][j] == '.':
            continue
        adj = adjacent(i, j)
        if len(adj) < 4:
            G[i][j] = '.'
            res2 += 1
            for a in adj:
                if a not in added:
                    added.add(a)
                    next_round.append(a)
    to_consider = next_round

print(res2)
