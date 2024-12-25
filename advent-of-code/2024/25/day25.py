import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/25/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
res = 0
locks, keys = [], []
for i in range(0, len(lines), 8):
    cols = [0] * 5
    if lines[i] == "#####":
        start, end, dir = i + 1, i + 7, 1
    else:
        start, end, dir = i + 5, i, -1

    for j in range(start, end, dir):
        for col in range(5):
            cols[col] += lines[j][col] == "#"
    if lines[i] == "#####":
        locks.append(cols)
    else:
        keys.append(cols)


for lock in locks:
    for key in keys:
        if all([lock[col] + key[col] <= 5 for col in range(5)]):
            res += 1

print(res)


# Part 2
res2 = 0
