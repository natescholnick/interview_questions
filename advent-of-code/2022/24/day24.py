import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2022/24/input.txt") as f:
    M = f.read().splitlines()

h = len(M) - 2
w = len(M[0]) - 2

# Part 1
# Observe that the valley is 25 x 120, meaning the blizzard positions repeat every 600 minutes
start, end = (0, 1), (h + 1, w)
tiles = {(i, j) for i in range(1, h + 1) for j in range(1, w + 1)}.union({start, end})
free_tiles = [tiles.copy() for _ in range(600)]
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if M[i][j] == ">":
            for t in range(600):
                # Remember to account for the 1, 1 shift caused by the border before modular reduction
                free_tiles[t].discard((i, 1 + (j + t - 1) % w))
        elif M[i][j] == "<":
            for t in range(600):
                free_tiles[t].discard((i, 1 + (j - t - 1) % w))
        elif M[i][j] == "^":
            for t in range(600):

                free_tiles[t].discard((1 + (i - t - 1) % h, j))
        elif M[i][j] == "v":
            for t in range(600):
                free_tiles[t].discard((1 + (i + t - 1) % h, j))


# Now with an O(1) lookup for tree paths, let's search
# Bfs works like a charm, although I ought to remember sooner next time:
# Even with revisiting, try out a seen/visited set!
# I spent so long bogged down by thousands of distinct paths for (pos, t) duplicates in the queue smh
def adj(p):
    # right, down, wait, up, left
    return [(p[0], p[1] + 1), (p[0] + 1, p[1]), p, (p[0] - 1, p[1]), (p[0], p[1] - 1)]


def bfs(start_pos, end_pos, start_time):
    seen = set()
    t = start_time
    q = deque([start_pos])
    end_time = None
    while not end_time:
        for _ in range(len(q)):
            pos = q.popleft()

            if pos == end_pos:
                end_time = t
                break

            if (pos, t) in seen:
                continue
            seen.add((pos, t))

            for neighbor in adj(pos):
                if neighbor in free_tiles[(t + 1) % 600]:
                    q.append(neighbor)
        t += 1

    return end_time


res = bfs(start, end, 0)
print(res)


# Part 2
return_time = bfs(end, start, res)
res2 = bfs(start, end, return_time)
print(res2)
