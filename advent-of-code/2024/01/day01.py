import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/01/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
res = 0
left, right = [], []

for line in lines:
    a, b = [int(x) for x in line.split(" ")]
    left.append(a)
    right.append(b)

left.sort()
right.sort()

for i in range(len(left)):
    res += abs(left[i] - right[i])

print(res)

# Part 2
count = Counter(right)
res2 = 0
for n in left:
    res2 += n * count[n]

print(res2)
