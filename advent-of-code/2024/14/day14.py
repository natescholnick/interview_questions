import os
import sys
from collections import defaultdict, deque, Counter, namedtuple
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/14/input.txt") as f:
    lines = f.read().splitlines()


width, height = 101, 103


def parse_line(line):
    p, v = line.split(" ")
    px, py = p[2:].split(",")
    vx, vy = v[2:].split(",")
    return (int(px), int(py), int(vx), int(vy))


# Part 1
# Quadrants, as per Euclidean plane:
# 2 | 1
# --+--
# 3 | 4
quads = [0] * 4
steps = 100
for line in lines:
    px, py, vx, vy = parse_line(line)
    x, y = (px + steps * vx) % width, (py + steps * vy) % height
    if x == width // 2 or y == height // 2:
        continue
    if y < height // 2:
        if x > width // 2:
            quads[0] += 1
        else:
            quads[1] += 1
    else:
        if x < width // 2:
            quads[2] += 1
        else:
            quads[3] += 1

res = 1
for quad in quads:
    res *= quad

print(res)

# Part 2
# Searching for x-symmertry isn't yielding anything...
# Let's search for horizontal lines
robots = []
for line in lines:
    robots.append([val for val in parse_line(line)])


# tick seconds in a modular loop
for second in range(width * height):
    M = [["."] * width for _ in range(height)]
    # move every robot
    for robot in robots:
        x, y, vx, vy = robot
        pos_x, pos_y = (x + second * vx) % width, (y + second * vy) % height
        M[pos_y][pos_x] = "#"
    for row in M:
        if "########" in "".join(row):
            for row in M:
                print("".join(row))
                res2 = second
            break

print(res2)
