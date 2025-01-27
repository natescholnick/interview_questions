import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2021/13/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
folds = []
points = []
is_Fold = False
for line in lines:
    if is_Fold:
        var = line.split("=")[0][-1]
        val = int(line.split("=")[1])
        # x counts columns, y rows
        folds.append((0, val) if var == "x" else (val, 0))
        continue
    if len(line) == 0:
        is_Fold = True
        continue
    point = tuple(int(x) for x in reversed(line.split(",")))
    points.append(point)


# folds are represented by their unique intersection point with an axis
def handleFold(fold, point):
    f_i, f_j = fold
    i, j = point
    if f_i == 0:
        if j < f_j:
            return point
        return (i, 2 * f_j - j)
    if i < f_i:
        return point
    return (2 * f_i - i, j)


def part1(x=1):
    folded_points = points[:]
    for fold in folds[:x]:
        curr_points = list(folded_points)
        folded_points = set()
        for point in curr_points:
            new_point = handleFold(fold, point)
            folded_points.add(new_point)
    return list(folded_points)


print(len(part1()))

# Part 2
m = n = 0
dots = part1(len(folds))
for i, j in dots:
    m = max(m, i)
    n = max(n, j)

M = [["."] * (n + 1) for _ in range(m + 1)]
for i, j in dots:
    M[i][j] = "#"

for row in range(m + 1):
    print("".join(M[row]))
