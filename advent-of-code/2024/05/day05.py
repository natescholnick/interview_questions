import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/05/input.txt") as f:
    input = f.read().split("\n\n")


# Part 1
rules, orders = input[0].splitlines(), input[1].splitlines()
before, after = defaultdict(list), defaultdict(list)

for rule in rules:
    b, a = rule.split("|")
    before[a].append(b)
    after[b].append(a)


def is_valid(order):
    for i in range(len(order) - 1):
        for j in range(i + 1, len(order)):
            if order[j] in before[order[i]]:
                return False
    return True


res = 0
for order in orders:
    o = order.split(",")
    if is_valid(o):
        res += int(o[len(o) // 2])

print(res)


# Part 2
def middle_after_reorder(seq):
    new = []
    pages_left = seq[:]
    while len(new) <= len(seq) // 2:
        for page in pages_left:
            if not any([p in before[page] for p in pages_left]):
                new.append(page)
                pages_left.remove(page)
                break

    return int(new[-1])


res2 = 0
for order in orders:
    o = order.split(",")
    if not is_valid(o):
        res2 += middle_after_reorder(o)

print(res2)
