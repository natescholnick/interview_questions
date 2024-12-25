import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/23/input.txt") as f:
    lines = f.read().splitlines()

G = defaultdict(set)

# Part 1
for line in lines:
    a, b = line.split("-")
    G[a].add(b)
    G[b].add(a)

tris = set()
for cpu1 in G:
    if cpu1[0] != "t":
        continue

    for cpu2 in G[cpu1]:
        for cpu3 in G[cpu2]:
            if cpu3 in G[cpu1]:
                tris.add(tuple(sorted([cpu1, cpu2, cpu3])))

print(len(tris))


# Part 2
# maximal clique problem means Bron-Kerbosch
# R = current clique, P = candidate set, X = exclusion set
cliques = set()


# no pivot needed
def bron_kerbosch(R, P, X):
    if not P and not X:
        cliques.add(tuple(sorted(R)))
    for node in P:
        if node in X:
            continue
        bron_kerbosch(R.union({node}), P.intersection(G[node]), X.intersection(G[node]))
        X.add(node)


bron_kerbosch(set(), set(G.keys()), set())

print(",".join(sorted(list(cliques), key=len)[-1]))
