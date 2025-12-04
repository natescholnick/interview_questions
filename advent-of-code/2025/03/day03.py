
import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2025/03/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
res = 0
for line in lines:
    m = len(line)
    first = max([x for x in line[:-1]])
    i = line.index(first)
    second = max([x for x in line[i+1:]])
    res += int(first + second)

print(res)

# Part 2
res2 = 0
for line in lines:
    m = len(line)
    value = ''
    i = 0
    for d in range(11, -1, -1):
        digit = max([x for x in line[i:m - d]])
        value += digit
        i = line.index(digit, i) + 1
    res2 += int(value)

print(res2)