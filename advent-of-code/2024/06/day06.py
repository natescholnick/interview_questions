import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/06/input.txt") as f:
    M = f.read().splitlines()

m = len(M)
M = [[c for c in M[i]] for i in range(m)]

for x in range(m):
    for y in range(m):
        if M[x][y] == "^":
            start_x, start_y = x, y
            break

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Part 1
curr_dir = 0
i, j = start_x, start_y
walked = set()
while i > 0 and i < m - 1 and j > 0 and j < m - 1:
    walked.add((i, j))
    di, dj = dirs[curr_dir]
    if M[i + di][j + dj] == "#":
        curr_dir = (curr_dir + 1) % 4
        di, dj = dirs[curr_dir]
    i += di
    j += dj

print(len(walked) + 1)


# Part 2
def is_cyclic(x, y, dir):
    i, j, curr = x, y, (dir + 1) % 4
    seen = set()
    while i > 0 and i < m - 1 and j > 0 and j < m - 1:
        if (i, j, curr) in seen or (i, j, curr) in visited:
            return True

        seen.add((i, j, curr))

        di, dj = dirs[curr]
        if M[i + di][j + dj] == "#":
            curr = (curr + 1) % 4
        else:
            i += di
            j += dj

    return False


res2 = 0
curr_dir = 0
i, j = start_x, start_y
visited = set()
while i > 0 and i < m - 1 and j > 0 and j < m - 1:
    di, dj = dirs[curr_dir]
    visited.add((i, j, curr_dir))

    # obstacle ahead
    if M[i + di][j + dj] == "#":
        curr_dir = (curr_dir + 1) % 4
    # check if an obstacle ahead creates a loop
    else:
        if M[i + di][j + dj] != "^":
            M[i + di][j + dj] = "#"
            res2 += is_cyclic(i, j, curr_dir)
        M[i + di][j + dj] = "^"
        i += di
        j += dj

print(res2)
