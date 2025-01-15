import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2022/22/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
is_map = True
G = []
w = max([len(line) for line in lines[:-2]])
for line in lines:
    if len(line) == 0:
        is_map = False
        continue
    if is_map:
        G.append([c for c in line] + [" "] * (w - len(line)))
    else:
        directions = line

directions = re.findall(r"\d+|\D+", directions)
directions = [int(x) if x.isdigit() else x for x in directions]

h = len(G)

start = None
left, right, up, down = {}, {}, {}, {}
for i in range(h):
    row_start = None
    for j in range(w):
        if G[i][j] == " ":
            continue
        if not start:
            start = (i, j)
        if not row_start:
            row_start = (i, j)
        if j == w - 1 or G[i][j + 1] == " ":
            right[(i, j)] = row_start
            left[row_start] = (i, j)


for j in range(w):
    col_start = None
    for i in range(h):
        if G[i][j] == " ":
            continue
        if not col_start:
            col_start = (i, j)
        if i == h - 1 or G[i + 1][j] == " ":
            down[(i, j)] = col_start
            up[col_start] = (i, j)


def step(loc, dir):
    if dir == "<":
        forward = left[loc] if loc in left else (loc[0], loc[1] - 1)
        return False if G[forward[0]][forward[1]] == "#" else forward
    if dir == ">":
        forward = right[loc] if loc in right else (loc[0], loc[1] + 1)
        return False if G[forward[0]][forward[1]] == "#" else forward
    if dir == "^":
        forward = up[loc] if loc in up else (loc[0] - 1, loc[1])
        return False if G[forward[0]][forward[1]] == "#" else forward
    if dir == "v":
        forward = down[loc] if loc in down else (loc[0] + 1, loc[1])
        return False if G[forward[0]][forward[1]] == "#" else forward


faces = [">", "v", "<", "^"]


def turn(dir, rot):
    if rot == "R":
        return faces[(faces.index(dir) + 1) % 4]
    return faces[(faces.index(dir) - 1) % 4]


facing = ">"
location = start
for instruction in directions:
    if isinstance(instruction, str):
        facing = turn(facing, instruction)
    else:
        while instruction and (next_step := step(location, facing)):
            location = next_step
            instruction -= 1

x, y = location
print(1000 * (x + 1) + 4 * (y + 1) + faces.index(facing))

# Part 2
# Imagine the cube like this, corners labeled to help see the folding:
#     1---2---3
#     | N | E |
#     4---+---5
#     | B |
# 4---+---5
# | W | S |
# 1---+---3
# | T |
# 2---3
# with faces North, East, Bottom, South, West, and Top
# Let's stitch together these edges!

cube_steps = {}
for i in range(50):
    # B <--> W
    cube_steps[(50 + i, 50, "<")] = (100, i, "v")
    cube_steps[(100, i, "^")] = (50 + i, 50, ">")
    # B <--> E
    cube_steps[(50 + i, 99, ">")] = (49, 100 + i, "^")
    cube_steps[(49, 100 + i, "v")] = (50 + i, 99, "<")
    # N <--> W
    cube_steps[(i, 50, "<")] = (149 - i, 0, ">")
    cube_steps[(149 - i, 0, "<")] = (i, 50, ">")
    # N <--> T
    cube_steps[(0, 50 + i, "^")] = (150 + i, 0, ">")
    cube_steps[(150 + i, 0, "<")] = (0, 50 + i, "v")
    # E <--> S
    cube_steps[(i, 149, ">")] = (149 - i, 99, "<")
    cube_steps[(149 - i, 99, ">")] = (i, 149, "<")
    # E <--> T
    cube_steps[(0, 100 + i, "^")] = (199, i, "^")
    cube_steps[(199, i, "v")] = (0, 100 + i, "v")
    # S <--> T
    cube_steps[(149, 50 + i, "v")] = (150 + i, 49, "<")
    cube_steps[(150 + i, 49, ">")] = (149, 50 + i, "^")


def take_cube_step(pos):
    if pos in cube_steps:
        forward = cube_steps[pos]
    elif pos[2] == "<":
        forward = (pos[0], pos[1] - 1, pos[2])
    elif pos[2] == ">":
        forward = (pos[0], pos[1] + 1, pos[2])
    elif pos[2] == "^":
        forward = (pos[0] - 1, pos[1], pos[2])
    elif pos[2] == "v":
        forward = (pos[0] + 1, pos[1], pos[2])
    return False if G[forward[0]][forward[1]] == "#" else forward


pos = (*start, ">")
for instruction in directions:
    if isinstance(instruction, str):
        pos = (pos[0], pos[1], turn(pos[2], instruction))
    else:
        while instruction and (next_step := take_cube_step(pos)):
            pos = next_step
            instruction -= 1

x, y, f = pos
print(1000 * (x + 1) + 4 * (y + 1) + faces.index(f))
