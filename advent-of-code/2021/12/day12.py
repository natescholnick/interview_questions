import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2021/12/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
G = defaultdict(list)
for line in lines:
    a, b = line.split("-")
    G[a].append(b)
    G[b].append(a)


def dfs(cave, path):
    if cave == "end":
        return 1

    if cave.islower() and cave in path:
        return 0

    return sum(dfs(nei, path + [cave]) for nei in G[cave])


print(dfs("start", []))


# Part 2
def dfs2(cave, path, hasRepeat):
    if cave == "end":
        return 1

    foundRepeat = hasRepeat
    if cave.islower() and cave in path:
        if hasRepeat or cave == "start":
            return 0
        foundRepeat = True

    return sum(dfs2(nei, path + [cave], foundRepeat) for nei in G[cave])


print(dfs2("start", [], False))
