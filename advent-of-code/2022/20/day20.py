import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2022/20/input.txt") as f:
    lines = f.read().splitlines()

m = len(lines)


# Part 1
seq = []
for i in range(m):
    seq.append((i, int(lines[i])))
    if lines[i] == "0":
        zero = (i, 0)

# basic idea: modding elements means we always move right
# so if we track the starting location to scan for the next element
# the amortized time complexity to find the next element is O(1)
start = 0
for i in range(m):
    while seq[start][0] != i:
        start += 1

    el = seq.pop(start)
    num = el[1] % (m - 1)
    insertion = (start + num) % (m - 1)
    seq.insert(insertion, el)

pivot = seq.index(zero)
print(sum([seq[(pivot + 1000 * x) % m][1] for x in range(1, 4)]))

# Part 2
loop = []
for i in range(m):
    loop.append((i, int(lines[i]) * 811589153))
    if lines[i] == "0":
        zero = (i, 0)

ref = loop[:]

for _ in range(10):
    for el in ref:
        i = loop.index(el)
        loop.pop(i)
        num = el[1] % (m - 1)
        insertion = (i + num) % (m - 1)
        loop.insert(insertion, el)

pivot = loop.index(zero)
print(sum([loop[(pivot + 1000 * x) % m][1] for x in range(1, 4)]))
