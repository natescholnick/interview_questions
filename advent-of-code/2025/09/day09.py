import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2025/09/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
res = 0
n = len(lines)
points = []
for line in lines:
    points.append(tuple(int(x) for x in line.split(",")))

for i in range(n - 1):
    x0, y0 = points[i]
    for j in range(i + 1, n):
        x1, y1 = points[j]
        res = max(res, (abs(x1 - x0) + 1) * (abs(y1 - y0) + 1))

print(res)

# Part 2
res2 = 0
