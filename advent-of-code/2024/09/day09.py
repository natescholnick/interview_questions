import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/09/input.txt") as f:
    disk = list(f.read())


# Part 1
l, r = 0, len(disk) - 1
new = []

r_used = 0
while l < r:
    size = int(disk[l])
    # file block, read from left
    if l % 2 == 0:
        id = l // 2
        for _ in range(size):
            new.append(id)
    # memory block, read from right
    else:
        r_size = int(disk[r])
        id = r // 2
        for _ in range(size):
            if r_used == r_size:
                r -= 2
                r_size, id, r_used = int(disk[r]), r // 2, 0
            r_used += 1
            new.append(id)

    l += 1

if l == r:
    new.extend([id] * (r_size - r_used))

res = 0
for i in range(len(new)):
    res += i * new[i]

print(res)

# Part 2
new = []
moved = set()

for i in range(len(disk)):
    size = int(disk[i])
    # mem block to fill
    if i % 2:
        # find file small enough
        j = len(disk) - 1
        while size > 0 and j > i:
            while j > i and (int(disk[j]) > size or j in moved):
                j -= 2
            # good file found
            if j > i:
                new.extend([j // 2] * int(disk[j]))
                size -= int(disk[j])
                moved.add(j)
                j = len(disk) - 1
            # no files fit
            else:
                new.extend(["."] * size)
    # file block
    else:
        char = "." if i in moved else i // 2
        new.extend([char] * size)

res2 = 0
for i in range(len(new)):
    if new[i] == ".":
        continue
    res2 += i * new[i]

print(res2)
