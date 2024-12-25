import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/11/input.txt") as f:
    line = [int(x) for x in f.read().split(" ")]

# Part 1
res = 0


def dfs(val, gen):
    if gen == 25:
        return 1
    if val == 0:
        return dfs(1, gen + 1)
    elif len(str(val)) % 2 == 0:
        return dfs(int(str(val)[: len(str(val)) // 2]), gen + 1) + dfs(
            int(str(val)[len(str(val)) // 2 :]), gen + 1
        )
    else:
        return dfs(val * 2024, gen + 1)


for stone in line:
    res += dfs(stone, 0)

print(res)


# Part 2
# cache: key = number on stone, value = # of descendents per generation (gen 0 is self)
cache = defaultdict(list)
res2 = 0
q = deque([])
for stone in line:
    q.append((stone, 0, []))

for gen in range(76):
    for stone in cache.keys():
        cache[stone].append(0)
    for i in range(len(q)):
        val, iter, path = q.popleft()
        # if we've seen this stone before, iterate through its cached descendent count
        if val in cache:
            num = cache[val][iter]
            q.append((val, iter + 1, path))
        else:
            num = 1
            cache[val].append(1)
            if val == 0:
                q.append((1, 0, path + [val]))
            elif len(str(val)) % 2 == 0:
                q.append((int(str(val)[: len(str(val)) // 2]), 0, path + [val]))
                q.append((int(str(val)[len(str(val)) // 2 :]), 0, path + [val]))
            else:
                q.append((val * 2024, 0, path + [val]))

        for anc in path:
            cache[anc][-1] += num


for stone in line:
    res2 += cache[stone][-1]

print(res2)
