import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/04/input.txt") as f:
    M = f.read().splitlines()


# Part 1
res = 0
m = len(M)


def read_all_directions(i, j):
    opts = []
    if i > 2:
        opts.append("".join(M[i - x][j] for x in range(4)))
        if j > 2:
            opts.append("".join(M[i - x][j - x] for x in range(4)))
        if j < m - 3:
            opts.append("".join(M[i - x][j + x] for x in range(4)))
    if i < m - 3:
        opts.append("".join(M[i + x][j] for x in range(4)))
        if j > 2:
            opts.append("".join(M[i + x][j - x] for x in range(4)))
        if j < m - 3:
            opts.append("".join(M[i + x][j + x] for x in range(4)))
    if j > 2:
        opts.append("".join(M[i][j - x] for x in range(4)))
    if j < m - 3:
        opts.append("".join(M[i][j + x] for x in range(4)))
    return opts


res = 0
for i in range(m):
    for j in range(m):
        if M[i][j] == "X":
            res += sum([opt == "XMAS" for opt in read_all_directions(i, j)])

print(res)

# Part 2
res2 = 0
for i in range(1, m - 1):
    for j in range(1, m - 1):
        if M[i][j] == "A":
            corners = (
                M[i - 1][j - 1] + M[i - 1][j + 1] + M[i + 1][j + 1] + M[i + 1][j - 1]
            )
            if corners in {"MMSS", "MSSM", "SMMS", "SSMM"}:
                res2 += 1
print(res2)
