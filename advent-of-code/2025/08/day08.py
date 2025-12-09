import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2025/08/input.txt") as f:
    lines = f.read().splitlines()


# Part 1
# Step 1: points -> sorted edges
def d(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2


points = []
for line in lines:
    points.append(tuple(int(x) for x in line.split(",")))

n = len(points)
distances = {}
for i in range(n - 1):
    for j in range(i + 1, n):
        distances[(i, j)] = d(points[i], points[j])

edges = sorted(distances.keys(), key=lambda x: distances[x])


# Step 2: Implement DSU to build and track circuit sizes
size = [1] * n
UF = {x: x for x in range(n)}


def find(u):
    if UF[u] == u:
        return u
    return find(UF[u])


def combine(u, v):
    u = find(u)
    v = find(v)
    if u == v:
        return

    if size[v] > size[u]:
        UF[u] = v
        size[v] += size[u]
        return size[v]

    UF[v] = u
    size[u] += size[v]
    return size[u]


# edge_count = 10
edge_count = 1000
for i in range(edge_count):
    u, v = edges[i]
    combine(u, v)

circuits = []
for i in range(n):
    if UF[i] == i:
        circuits.append(size[i])

circuits.sort(reverse=True)
print(circuits[0] * circuits[1] * circuits[2])

# Part 2
res2 = None
for i in range(edge_count, len(edges)):
    u, v = edges[i]
    if combine(u, v) == n:
        res2 = points[u][0] * points[v][0]
        break

print(res2)
