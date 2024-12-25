import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/03/input.txt") as f:
    lines = f.read().splitlines()


# Part 1
res = 0
for line in lines:
    loc = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
    for a, b in loc:
        res += int(a) * int(b)

print(res)

# Part 2
res2 = 0
enabler = 1
for line in lines:
    loc = re.finditer(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
    for item in loc:
        if item.group() == "do()":
            enabler = 1
        elif item.group() == "don't()":
            enabler = 0
        else:
            a, b = [int(x) for x in item.group()[4:-1].split(",")]
            res2 += enabler * a * b


print(res2)
