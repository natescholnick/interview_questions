import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2025/01/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
val = 50
res = 0
for line in lines:
    dir = line[0]
    add = int(line[1:])
    if dir == "L":
        val -= add
    else:
        val += add

    val %= 100
    if not val:
        res += 1

print(res)


# Part 2
def cross_zero(a, b, mod=100):
    if b > a:
        return b // mod

    if b > 0:
        return 0

    return -((b - 1) // 100) - (a == 0)


res2 = 0
val = 50
for line in lines:
    dir = line[0]
    add = int(line[1:])
    prev = val
    if dir == "L":
        val -= add
    else:
        val += add

    res2 += cross_zero(prev, val)
    val %= 100

print(res2)
