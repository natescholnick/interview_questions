import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/18/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
m = 71
M = [["."] * m for _ in range(m)]

for i in range(1024):
    x, y = [int(a) for a in lines[i].split(",")]
    M[y][x] = "#"

q = deque([])
q.append((0, 0, 0))
cache = defaultdict(lambda: sys.maxsize)

while q:
    i, j, steps = q.popleft()
    if i < 0 or i >= m or j < 0 or j >= m or M[i][j] == "#" or cache[(i, j)] <= steps:
        continue
    cache[(i, j)] = steps
    q.append((i + 1, j, steps + 1))
    q.append((i - 1, j, steps + 1))
    q.append((i, j + 1, steps + 1))
    q.append((i, j - 1, steps + 1))

print(cache[(m - 1, m - 1)])

# Part 2
visited = set()


def find_exit():
    q = deque([])
    q.append((0, 0))
    visited = set()

    while q:
        i, j = q.popleft()
        if i < 0 or i >= m or j < 0 or j >= m or M[i][j] == "#" or (i, j) in visited:
            continue
        visited.add((i, j))
        if i == m - 1 and j == m - 1:
            return True
        q.append((i + 1, j))
        q.append((i - 1, j))
        q.append((i, j + 1))
        q.append((i, j - 1))

    return False


res2 = 0
for i in range(1024, len(lines)):
    x, y = [int(a) for a in lines[i].split(",")]
    M[y][x] = "#"
    if not find_exit():
        res2 = i
        break

print(lines[res2])
