import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2025/05/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
res = 0
ids_start = 0
ranges = []
for i in range(len(lines)):
    if lines[i] == "":
        ids_start = i + 1
        break
    l, r = [int(x) for x in lines[i].split("-")]
    ranges.append((l, r))

ranges.sort()
on_off_array = []
for start, end in ranges:
    if not on_off_array or start > on_off_array[-1] + 1:
        on_off_array.append(start)
        on_off_array.append(end)
    else:
        on_off_array[-1] = max(on_off_array[-1], end)

for i in range(ids_start, len(lines)):
    ingredient = int(lines[i])
    index = bisect.bisect_left(on_off_array, ingredient)
    if index % 2:
        res += 1
    else:
        res += index < len(on_off_array) and ingredient == on_off_array[index]

print(res)


# Part 2
# Sometimes you get lucky and coincidentally solve part 2 during part 1
res2 = 0
for i in range(0, len(on_off_array), 2):
    res2 += on_off_array[i + 1] - on_off_array[i] + 1

print(res2)
