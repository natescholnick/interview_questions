import os
from collections import defaultdict, deque, Counter
import re

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/13/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
def checkSym(grid):
    for i in range(len(grid) - 1):
        sym = True
        l, r = i, i+1
        while l >= 0 and r < len(grid):
            if grid[l] == grid[r]:
                l -= 1
                r += 1
            else:
                sym = False
                break
        if sym:
            return i + 1
    return 0

res = 0
G = []
for line in lines:
    if len(line) != 0:
        G.append(line)
    else:
        res += 100 * checkSym(G)
        res += checkSym(list(zip(*reversed(G))))
        G = []
res += 100 * checkSym(G)
res += checkSym(list(zip(*reversed(G))))
print(res)


# Part 2
def oneOff(s1, s2):
    ok = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if ok:
                return False
            ok = True
    return ok


def checkSmudge(grid):
    for i in range(len(grid) - 1):
        smudge = False
        l, r = i, i+1
        while l >= 0 and r < len(grid):
            if grid[l] == grid[r]:
                l -= 1
                r += 1
            elif oneOff(grid[l], grid[r]):
                if smudge:
                    smudge = False
                    break
                l -= 1
                r += 1
                smudge = True
            else:
                smudge = False
                break
        if smudge:
            return i + 1
    return 0

res2 = 0
G = []
for line in lines:
    if len(line) != 0:
        G.append(line)
    else:
        res2 += 100 * checkSmudge(G)
        res2 += checkSmudge(list(zip(*reversed(G))))
        G = []
res2 += 100 * checkSmudge(G)
res2 += checkSmudge(list(zip(*reversed(G))))
print(res2)