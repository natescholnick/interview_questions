import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2025/02/input.txt") as f:
    line = f.read()

# Part 1
res = 0
ranges = line.split(",")
for r in ranges:
    a, b = [int(x) for x in r.split("-")]
    for val in range(a, b + 1):
        s = str(val)
        if len(s) % 2:
            continue
        if s[: len(s) // 2] == s[len(s) // 2 :]:
            res += val

print(res)

# Part 2
res2 = 0


def check_invalid(s):
    m = len(s)
    for i in range(m // 2):
        sub_s = s[: i + 1]
        if sub_s * (m // len(sub_s)) == s:
            return int(s)
    return 0


for r in ranges:
    a, b = [int(x) for x in r.split("-")]
    for val in range(a, b + 1):
        s = str(val)
        res2 += check_invalid(s)

print(res2)
