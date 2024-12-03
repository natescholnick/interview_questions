import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/02/input.txt") as f:
    lines = f.read().splitlines()


# Part 1
def isSafe(report):
    for i in range(len(report) - 1):
        dir = 1 if report[1] < report[0] else -1
        if (
            dir * (report[i] - report[i + 1]) < 1
            or dir * (report[i] - report[i + 1]) > 3
        ):
            return False

    return True


res = 0
for line in lines:
    res += isSafe([int(x) for x in line.split(" ")])

print(res)


# Part 2
def isSafe2(report):
    reports = [report[:i] + report[i + 1 :] for i in range(len(report) - 1)] + [
        report[:-1]
    ]
    return any(isSafe(r) for r in reports)


res2 = 0
for line in lines:
    res2 += isSafe2([int(x) for x in line.split(" ")])

print(res2)
