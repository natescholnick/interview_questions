import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/16/input.txt") as f:
    M = f.read().splitlines()

m = len(M)

# E, S, W, N
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Part 1
for i in range(m):
    for j in range(m):
        if M[i][j] == "S":
            start_i, start_j = i, j
        elif M[i][j] == "E":
            end_i, end_j = i, j

# i, j, dir, score
q = deque([])
cache = defaultdict(lambda: sys.maxsize)
q.append((start_i, start_j, 0, 0))
while q:
    i, j, dir, score = q.popleft()
    if (i, j, dir) in cache and cache[(i, j, dir)] <= score:
        continue
    cache[(i, j, dir)] = score
    # move straight
    di, dj = dirs[dir]
    if M[i + di][j + dj] != "#":
        q.append((i + di, j + dj, dir, score + 1))
    # turns
    q.append((i, j, (dir + 1) % 4, score + 1000))
    q.append((i, j, (dir - 1) % 4, score + 1000))

print(
    min(
        cache[(end_i, end_j, 0)],
        cache[(end_i, end_j, 1)],
        cache[(end_i, end_j, 2)],
        cache[(end_i, end_j, 3)],
    )
)

# Part 2
res = sys.maxsize
# edge case: multiple best paths converge at exit
best_exits = set()
for dir in range(4):
    if cache[(end_i, end_j, dir)] < res:
        res = cache[(end_i, end_j, dir)]
        best_exits = {(end_i, end_j, dir)}
    elif cache[(end_i, end_j, dir)] == res:
        best_exits.add(((end_i, end_j, dir)))

en_route = {(start_i, start_j, 0)}.union(best_exits)


def dfs(i, j, dir, score, path):
    # not best path
    if score > cache[(i, j, dir)] or score > res:
        return
    # success, done
    if (i, j, dir) != (start_i, start_j, 0) and (i, j, dir) in en_route:
        for tile in path:
            en_route.add(tile)
        return
    di, dj = dirs[dir]
    if M[i + di][j + dj] != "#":
        dfs(i + di, j + dj, dir, score + 1, path + [(i, j, dir)])
    dfs(i, j, (dir + 1) % 4, score + 1000, path + [(i, j, dir)])
    dfs(i, j, (dir - 1) % 4, score + 1000, path + [(i, j, dir)])


dfs(start_i, start_j, 0, 0, [])
seats = set()
for i, j, dir in en_route:
    seats.add((i, j))
print(len(seats))
