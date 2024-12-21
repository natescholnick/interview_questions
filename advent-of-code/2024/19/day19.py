import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/19/input.txt") as f:
    lines = f.read().splitlines()

towels = set(lines[0].split(", "))
patterns = lines[2:]
# Part 1
cache = {towel: True for towel in towels}
possible = []


def can_make(pattern):
    if pattern in cache:
        return cache[pattern]
    cache[pattern] = False
    for i in range(1, len(pattern)):
        if pattern[:i] in towels:
            cache[pattern] |= can_make(pattern[i:])
    return cache[pattern]


res = 0
for pattern in patterns:
    if can_make(pattern):
        possible.append(pattern)
        res += 1

print(res)

# Part 2
cache = {}


def count_makes(pattern):
    if pattern in cache:
        return cache[pattern]
    cache[pattern] = 0
    for i in range(1, len(pattern)):
        if pattern[:i] in towels:
            cache[pattern] += count_makes(pattern[i:])
    return cache[pattern]


for towel in sorted(towels, key=lambda x: len(x)):
    if len(towel) == 1:
        cache[towel] = 1
    else:
        count_makes(towel)
        cache[towel] += 1

res2 = 0
for pattern in possible:
    res2 += count_makes(pattern)

print(res2)
