import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import functools
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2025/06/input.txt") as f:
    lines = f.read().splitlines()

G = []
# Part 1
res = 0
for line in lines:
    clean_line = re.sub(r"\s+", " ", line)
    G.append(clean_line.strip().split(" "))


m = len(G) - 1
n = len(G[0])
for col in range(n):
    if G[-1][col] == "+":
        res += sum([int(G[row][col]) for row in range(m)])
    else:
        res += functools.reduce(
            lambda x, y: x * y, [int(G[row][col]) for row in range(m)]
        )

print(res)

# Part 2
res2 = 0
n = len(lines[0])
nums = []
num = ""
op = "+"
for col in range(n - 1, -1, -1):
    reset = True
    for row in range(m):
        if lines[row][col] != " ":
            reset = False
            num += lines[row][col]
    if reset:
        if op == "+":
            res2 += sum(nums)
        else:
            res2 += functools.reduce(lambda x, y: x * y, nums)
        nums = []
    else:
        nums.append(int(num))
        if lines[m][col] != " ":
            op = lines[m][col]
    num = ""


if op == "+":
    res2 += sum(nums)
else:
    res2 += functools.reduce(lambda x, y: x * y, nums)

print(res2)
