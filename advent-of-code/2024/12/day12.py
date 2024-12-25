import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/12/input.txt") as f:
    M = f.read().splitlines()

m = len(M)

# Part 1
res = 0
seen = set()


def dfs(i, j, type):
    if i < 0 or i >= m or j < 0 or j >= m or M[i][j] != type:
        return 0, 1
    if (i, j) in seen:
        return 0, 0
    a, p = 1, 0
    seen.add((i, j))
    for adj_i, adj_j in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        adj_a, adj_p = dfs(adj_i, adj_j, type)
        a += adj_a
        p += adj_p
    return a, p


for i in range(m):
    for j in range(m):
        if (i, j) not in seen:
            area, perimeter = dfs(i, j, M[i][j])
            res += area * perimeter

print(res)

# Part 2
# fundamental insight: # sides == # corners, which are easier to count
res2 = 0
seen = set()
# up, right, down, left
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_same(i, j, type):
    if i < 0 or i >= m or j < 0 or j >= m or M[i][j] != type:
        return False
    return True


def dfs2(i, j, type):
    if (i, j) in seen or not is_same(i, j, type):
        return 0, 0
    seen.add((i, j))
    a, c = 1, 0
    for dir in range(4):
        li, lj = dirs[dir]
        ri, rj = dirs[(dir + 1) % 4]
        # if two adjacent edges are not in the same region, that indicates a convex corner
        if not is_same(i + li, j + lj, type) and not is_same(i + ri, j + rj, type):
            c += 1
        # if two adjacent edges are in same region, but the diagonal is outside, that indicates a concave corner
        if (
            is_same(i + li, j + lj, type)
            and is_same(i + ri, j + rj, type)
            and not is_same(i + li + ri, j + lj + rj, type)
        ):
            c += 1

    for adj_i, adj_j in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        adj_a, adj_c = dfs2(adj_i, adj_j, type)
        a += adj_a
        c += adj_c
    return a, c


for i in range(m):
    for j in range(m):
        if (i, j) not in seen:
            area, corners = dfs2(i, j, M[i][j])
            res2 += area * corners

print(res2)
