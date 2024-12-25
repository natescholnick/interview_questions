import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/07/input.txt") as f:
    lines = f.read().splitlines()


# Part 1
def dfs(i, val, args, ans):
    if i == len(args) and val == ans:
        return True
    if val > ans or i == len(args):
        return False

    return dfs(i + 1, val + args[i], args, ans) or dfs(i + 1, val * args[i], args, ans)


res = 0
for line in lines:
    ans, args = line.split(": ")
    ans = int(ans)
    args = [int(x) for x in args.split(" ")]
    if dfs(1, args[0], args, ans):
        res += ans

print(res)


# Part 2
def dfs2(i, val, args, ans):
    if i == len(args) and val == ans:
        return True
    if val > ans or i == len(args):
        return False

    return (
        dfs2(i + 1, val + args[i], args, ans)
        or dfs2(i + 1, val * args[i], args, ans)
        or dfs2(i + 1, int(str(val) + str(args[i])), args, ans)
    )


res2 = 0
for line in lines:
    ans, args = line.split(": ")
    ans = int(ans)
    args = [int(x) for x in args.split(" ")]
    if dfs2(1, args[0], args, ans):
        res2 += ans

print(res2)
