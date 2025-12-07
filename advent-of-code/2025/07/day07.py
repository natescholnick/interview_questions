import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2025/07/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
res = 0
m = len(lines)
n = len(lines[0])
G = [[c for c in line] for line in lines]

for j in range(n):
    if G[0][j] == "S":
        G[1][j] = "|"

for i in range(2, m):
    for j in range(n):
        if G[i - 1][j] == "|":
            if G[i][j] == "^":
                G[i][j - 1] = "|"
                G[i][j + 1] = "|"
                res += 1
            else:
                G[i][j] = "|"

# for row in G:
#     print("".join(row))

print(res)


# Part 2
# idea: Replace '|' with timeline count
G2 = [[0 if c == "." else c for c in line] for line in lines]

for j in range(n):
    if G2[0][j] == "S":
        G2[1][j] = 1

for i in range(2, m):
    for j in range(n):
        inc = G2[i - 1][j]
        if inc and isinstance(inc, int):
            if G2[i][j] == "^":
                G2[i][j - 1] += inc
                G2[i][j + 1] += inc
            else:
                G2[i][j] += inc


print(sum(G2[-1]))
