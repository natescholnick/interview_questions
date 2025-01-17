import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2022/23/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
# seize this rare opportunity to use Cartesian coordinates instead of matrix coordinates!
m = len(lines)
elves = set()
for x in range(m):
    for y in range(m):
        if lines[m - y - 1][x] == "#":
            elves.add((x, y))


moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
next_round = set()
seen = set()


# will an elf propose moving in a given cardinal direcrion?
def check_direction(x, y, dir):
    dx, dy = moves[dir]
    # adjacent
    tiles = [(x + dx, y + dy)]
    # diagonals
    tiles.extend(
        [(x + 1, y + dy), (x - 1, y + dy)]
        if dx == 0
        else [(x + dx, y + 1), (x + dx, y - 1)]
    )

    if all([tile not in elves for tile in tiles]):
        return (x + dx, y + dy)


def determine_proposal(x, y, round):
    global elf_moved
    alone = True
    for a in range(-1, 2):
        for b in range(-1, 2):
            if a == 0 and b == 0:
                continue
            alone &= (x + a, y + b) not in elves
    if alone:
        return

    elf_moved = True

    for d in range(round, round + 4):
        if proposal := check_direction(x, y, d % 4):
            return proposal


def dfs_paths(elf, prop):
    paths = []
    for dx, dy in ((0, 1), (0, -1), (-1, 0), (1, 0)):
        tile = (prop[0] + dx, prop[1] + dy)
        if tile != elf and tile in elves:
            paths.append(tile)

    return paths


# Alright, enough helper functions! The plan:
# DFS from an elf we haven't seen yet. Determine their proposal. Now DFS knowing that proposal for all elves adjacent to the proposal.
# Through this process, we can determine where each elf will move without iterating separately for proposal and movement
def dfs(elf, inc_prop, round):
    seen.add(elf)
    prop = determine_proposal(*elf, round)
    # already spread out, or nowhere to go
    if not prop:
        next_round.add(elf)
        return

    # proposal conflict with recursive parent
    if prop == inc_prop:
        next_round.add(elf)
    else:
        # proposal conflict with recursive child
        if any(
            [dfs(neighbor, prop, round) == prop for neighbor in dfs_paths(elf, prop)]
        ):
            next_round.add(elf)
        else:
            next_round.add(prop)

    # no matter what, we return the proposal to be checked against up the chain
    return prop


for round in range(10):
    for elf in elves:
        if elf in seen:
            continue
        dfs(elf, None, round)

    elves, next_round, seen = next_round, set(), set()

# get rectangle bounds
x1 = x2 = y1 = y2 = 0
for x, y in elves:
    x1 = min(x1, x)
    x2 = max(x2, x)
    y1 = min(y1, y)
    y2 = max(y2, y)

# non-elf spaces in rectangle
print((x2 - x1 + 1) * (y2 - y1 + 1) - len(elves))

# Part 2
# Note that we are starting in the 11th round following part 1
elf_moved = True
round = 10
while elf_moved:
    elf_moved = False
    for elf in elves:
        if elf in seen:
            continue
        dfs(elf, None, round)

    elves, next_round, seen = next_round, set(), set()
    round += 1

print(round)
