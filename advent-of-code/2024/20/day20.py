import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/20/input.txt") as f:
    M = f.read().splitlines()

m = len(M)
for i in range(m):
    for j in range(m):
        if M[i][j] == "S":
            i_start, j_start = i, j
        if M[i][j] == "E":
            i_end, j_end = i, j


# Part 1
def bfs(i0, j0):
    cache = defaultdict(lambda: sys.maxsize)
    q = deque([])
    q.append((i0, j0, 0))
    while q:
        i, j, time = q.popleft()
        if (
            i < 0
            or i >= m
            or j < 0
            or j >= m
            or M[i][j] == "#"
            or cache[(i, j)] <= time
        ):
            continue
        cache[(i, j)] = time
        for i1, j1 in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            q.append((i1, j1, time + 1))
    return cache


time_from_start = bfs(i_start, j_start)
time_from_end = bfs(i_end, j_end)
honest = time_from_start[(i_end, j_end)]


def jumps(i, j):
    return filter(
        lambda x: x[0] > 0
        and x[1] > 0
        and x[0] <= m
        and x[1] <= m
        and (x[0], x[1]) in time_from_end,
        [
            (i + 2, j),
            (i - 2, j),
            (i, j + 2),
            (i, j - 2),
            (i + 1, j + 1),
            (i + 1, j - 1),
            (i - 1, j + 1),
            (i - 1, j - 1),
        ],
    )


cheats = defaultdict(int)
for i in range(m):
    for j in range(m):
        if (i, j) not in time_from_start:
            continue
        for i1, j1 in jumps(i, j):
            time_saved = honest - (
                time_from_start[(i, j)] + time_from_end[(i1, j1)] + 2
            )
            if time_saved > 0:
                cheats[time_saved] += 1

res = 0
for cheat in cheats:
    if cheat >= 100:
        res += cheats[cheat]

print(res)


# Part 2
# runtime wasn't good, close to a minute, but hey :)
def d(p0, p1):
    return abs(p0[0] - p1[0]) + abs(p0[1] - p1[1])


time_saved = 100
res2 = 0
for p0, t0 in time_from_start.items():
    for p1, t1 in time_from_end.items():
        dist = d(p0, p1)
        if dist > 20:
            continue
        res2 += t0 + dist + t1 + time_saved <= honest

print(res2)
