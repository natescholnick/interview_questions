import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/15/input.txt") as f:
    lines = f.read().splitlines()


dirs = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1),
}

# Part 1
M = []
moves = []
for i in range(len(lines)):
    if len(lines[i]) == 0:
        pass
    elif lines[i][0] == "#":
        M.append([c for c in lines[i]])
        if "@" in lines[i]:
            start_i = i
            start_j = lines[i].index("@")
    else:
        moves.extend([move for move in lines[i]])

m = len(M)


def move_robot(i0, j0, dir):
    i, j = i0, j0
    di, dj = dirs[dir]
    # look ahead to check for space to move
    while M[i + di][j + dj] == "O":
        i += di
        j += dj
    # no movement
    if M[i + di][j + dj] == "#":
        return i0, j0
    # move the chain of boxes
    while i != i0 or j != j0:
        M[i + di][j + dj] = M[i][j]
        i -= di
        j -= dj
    # move the robot
    M[i + di][j + dj] = "@"
    M[i0][j0] = "."
    return i0 + di, j0 + dj


res = 0
i, j = start_i, start_j
for move in moves:
    i, j = move_robot(i, j, move)

for i in range(m):
    for j in range(m):
        if M[i][j] == "O":
            res += 100 * i + j

print(res)

# Part 2
M = []
moves = []
for i in range(len(lines)):
    if len(lines[i]) == 0:
        pass
    elif lines[i][0] == "#":
        line = []
        for c in lines[i]:
            if c == "#":
                line.extend(["#"] * 2)
            elif c == ".":
                line.extend(["."] * 2)
            if c == "O":
                line.extend(["[", "]"])
            if c == "@":
                line.extend(["@", "."])
                start_i = i
                start_j = lines[i].index("@") * 2
        M.append(line)
    else:
        moves.extend([move for move in lines[i]])

m = len(M)


# basically part 1
def move_robot_j(i0, j0, dir):
    i, j = i0, j0
    dj = dirs[dir][1]
    # look ahead to check for space to move
    while M[i][j + dj] != "." and M[i][j + dj] != "#":
        j += dj
    # no movement
    if M[i][j + dj] == "#":
        return i0, j0
    # move the chain of boxes
    while j != j0:
        M[i][j + dj] = M[i][j]
        j -= dj
    # move the robot
    M[i][j + dj] = "@"
    M[i0][j0] = "."
    return i0, j0 + dj


# handle the more complex vertical movement
def move_robot_i(i0, j0, dir):
    i, j = i0, j0
    di = dirs[dir][0]

    # No box cases
    if M[i + di][j] == "#":
        return i0, j0
    if M[i + di][j] == ".":
        M[i][j], M[i + di][j] = ".", "@"
        return i0 + di, j0

    # scan the box cluster
    cluster = []
    q = deque([])
    q.append((i0, j0))
    while q:
        cluster.append(set())
        for _ in range(len(q)):
            i, j = q.popleft()
            cluster[-1].add((i, j))
            next_block = M[i + di][j]
            # cluster blocked
            if next_block == "#":
                return i0, j0
            if next_block == "[":
                q.append((i + di, j))
                q.append((i + di, j + 1))
            elif next_block == "]":
                q.append((i + di, j))
                q.append((i + di, j - 1))

    for x in range(len(cluster) - 1, -1, -1):
        for i, j in cluster[x]:
            # move block vertically
            M[i + di][j] = M[i][j]
            if x == 0 or (i - di, j) not in cluster[x - 1]:
                M[i][j] = "."
    return i0 + di, j0


res2 = 0
i, j = start_i, start_j
for move in moves:
    if move in {"<", ">"}:
        i, j = move_robot_j(i, j, move)
    else:
        i, j = move_robot_i(i, j, move)

for row in M:
    print("".join(row))

for i in range(m):
    for j in range(2 * m):
        if M[i][j] == "[":
            res2 += 100 * i + j

print(res2)
