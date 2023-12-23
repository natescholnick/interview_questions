import os
from collections import defaultdict, deque, Counter
import re
import heapq
import math

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2021/11/input.txt") as f:
    G = f.read().splitlines()


# Part 1
m = len(G)
for row in range(m):
    G[row] = [int(x) for x in G[row]]

def doStep() -> int:
    flashed = set()
    q = deque([])
    for i in range(m):
        for j in range(m):
            G[i][j] += 1
            if G[i][j] > 9:
                q.append((i, j))

    # enqueued octopi are flashing OR gaining power from adjacent flashes
    while q:
        i, j = q.popleft()
        if i < 0 or j < 0 or i >= m or j >= m or (i, j) in flashed:
            continue
        G[i][j] += 1
        if G[i][j] > 9:
            G[i][j] = 0
            flashed.add((i, j))
            q.extend([(i+di, j+dj) for di in (-1, 0, 1) for dj in [-1, 0, 1]])

    return len(flashed)

res = 0
for _ in range(100):
    res += doStep()

print(res)

# Part 2, first attempting brute force
res2 = 101
while doStep() != 100:
    res2 += 1

print(res2)