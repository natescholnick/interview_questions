import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np
import matplotlib.pyplot as plt

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
# For this part, we make use of the observation that the points trace a path counterclockwise
# That is, if we consider points A, B, and C:
#
#  A-----B
#  |
#  |
#  |
#  C
#
# If the points appear in the order BAC,
# This is a convex section and green tiles are to the right of A
# Oppositely, if the points appear in the order CAB,
# This is a concave section and green tiles are to the left of A
res2 = 0


def define_edge(p1, p2):
    p1 %= n
    p2 %= n
    if p1 == p2:
        raise ValueError("Comparing the same point")
    x1, y1 = points[p1]
    x2, y2 = points[p2]
    if x1 == x2:
        return "U" if y2 > y1 else "D"
    return "R" if x2 > x1 else "L"


def define_corner(i):
    return define_edge(i - 1, i) + define_edge(i, i + 1)


prev = points[-1]
edges = []
corners = []
for i in range(n):
    corners.append(define_corner(i))
    x, y = points[i]
    if prev[0] == x:
        edges.append((*sorted([prev[1], y]), x))
    else:
        edges.append((*sorted([prev[0], x]), y))

    prev = points[i]

convex = {"DR", "RU", "UL", "LD"}
concave = {"RD", "UR", "LU", "DL"}


def find_vert(start, di, y_intercept, bound):
    # line up point
    if define_edge(start, start + di) not in {"U", "D"}:
        start += di
        start %= n
    # does a green edge only extend to the next point?
    if define_corner(start) in convex:
        return points[start][0]
    j = start
    while True:
        j += 2 * di
        j %= n
        if (bound > 0 and points[j][0] < bound) or (
            bound < 0 and points[j][0] > -bound
        ):
            continue
        bot, top = sorted([points[j][1], points[(j + di) % n][1]])
        if y_intercept > bot and y_intercept < top:
            return points[j][0]


def find_horiz(start, di, x_intercept, bound):
    # line up point
    if define_edge(start, start + di) not in {"L", "R"}:
        start += di
        start %= n
    # does a green edge only extend to the next point?
    if define_corner(start) in convex:
        return points[start][1]
    j = start
    while True:
        j += 2 * di
        j %= n
        if (bound > 0 and points[j][1] < bound) or (
            bound < 0 and points[j][1] > -bound
        ):
            continue
        bot, top = sorted([points[j][0], points[(j + di) % n][0]])
        if x_intercept > bot and x_intercept < top:
            return points[j][1]


extends = []  # l, r, d, u
for i in range(n):
    x, y = points[i]
    corner = corners[i]
    extends.append([x, x, y, y])

    # convex corners (only extends in two directions)
    if corner == "DR":
        extends[-1][1] = find_vert(i, 1, y, x)
        extends[-1][3] = find_horiz(i, -1, x, y)
    if corner == "RU":
        extends[-1][3] = find_horiz(i, 1, x, y)
        extends[-1][0] = find_vert(i, -1, y, -x)
    if corner == "UL":
        extends[-1][0] = find_vert(i, 1, y, -x)
        extends[-1][2] = find_horiz(i, -1, x, -y)
    if corner == "LD":
        extends[-1][2] = find_horiz(i, 1, x, -y)
        extends[-1][1] = find_vert(i, -1, y, x)

    # concave corners (extends in 4 directions)
    if corner == "RD":
        extends[-1][0] = find_vert(i, -1, y, -x)
        extends[-1][1] = find_vert(i, 1, y, x)
        extends[-1][2] = find_horiz(i, 1, x, -y)
        extends[-1][3] = find_horiz(i, -1, x, y)
    if corner == "UR":
        extends[-1][0] = find_vert(i, -1, y, -x)
        extends[-1][1] = find_vert(i, 1, y, x)
        extends[-1][2] = find_horiz(i, -1, x, -y)
        extends[-1][3] = find_horiz(i, 1, x, y)
    if corner == "LU":
        extends[-1][0] = find_vert(i, 1, y, -x)
        extends[-1][1] = find_vert(i, -1, y, x)
        extends[-1][2] = find_horiz(i, -1, x, -y)
        extends[-1][3] = find_horiz(i, 1, x, y)
    if corner == "DL":
        extends[-1][0] = find_vert(i, 1, y, -x)
        extends[-1][1] = find_vert(i, -1, y, x)
        extends[-1][2] = find_horiz(i, 1, x, -y)
        extends[-1][3] = find_horiz(i, -1, x, y)

xs = np.array([p[0] for p in points])
ys = np.array([p[1] for p in points])

plt.plot(xs, ys)
plt.show()

# 94634,50269
# 94634,48484
floor = points[248][1]
ceil = points[249][1]

for i in range(30, 248):
    extends[i][2] = max(extends[i][2], floor)

for i in range(250, 467):
    extends[i][3] = min(extends[i][3], ceil)

for i in range(n - 1):
    x0, y0 = points[i]
    for j in range(i + 1, n):
        x1, y1 = points[j]
        if (
            (extends[i][0] <= x1 and extends[i][1] >= x1)
            and (extends[i][2] <= y1 and extends[i][3] >= y1)
            and (extends[j][0] <= x0 and extends[j][1] >= x0)
            and (extends[j][2] <= y0 and extends[j][3] >= y0)
        ):
            res2 = max(res2, (abs(x1 - x0) + 1) * (abs(y1 - y0) + 1))

print(res2)
