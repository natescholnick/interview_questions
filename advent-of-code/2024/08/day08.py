import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/08/input.txt") as f:
    G = f.read().splitlines()


# Part 1
m, n = len(G), len(G[0])
nodes = defaultdict(list)
for i in range(m):
    for j in range(n):
        if G[i][j] != ".":
            nodes[G[i][j]].append((i, j))

# antinodes = set()
# for coords in nodes.values():
#     for i in range(len(coords) - 1):
#         # P1 = (x1, y1)
#         x1, y1 = coords[i]
#         for j in range(i + 1, len(coords)):
#             # P2 = (x2, y2)
#             x2, y2 = coords[j]
#             dx, dy = x1 - x2, y1 - y2
#             # For a geometric interpretation, handy: the vector P1 - P2 goes from P2 to P1
#             p1, p2 = x1 + dx, y1 + dy
#             if p1 >= 0 and p1 < m and p2 >= 0 and p2 < n:
#                 antinodes.add((p1, p2))
#             p1, p2 = x2 - dx, y2 - dy
#             if p1 >= 0 and p1 < m and p2 >= 0 and p2 < n:
#                 antinodes.add((p1, p2))

# print(len(antinodes))

# Part 2
antinodes = set()
for coords in nodes.values():
    for i in range(len(coords) - 1):
        # P1 = (x1, y1)
        x1, y1 = coords[i]
        for j in range(i + 1, len(coords)):
            # P2 = (x2, y2)
            x2, y2 = coords[j]
            dx, dy = x1 - x2, y1 - y2
            # For a geometric interpretation, handy: the vector P1 - P2 goes from P2 to P1
            p1, p2 = x1, y1
            while p1 >= 0 and p1 < m and p2 >= 0 and p2 < n:
                antinodes.add((p1, p2))
                p1 += dx
                p2 += dy
            p1, p2 = x2, y2
            while p1 >= 0 and p1 < m and p2 >= 0 and p2 < n:
                antinodes.add((p1, p2))
                p1 -= dx
                p2 -= dy

print(len(antinodes))
