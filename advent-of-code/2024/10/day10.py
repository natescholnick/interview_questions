import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/10/input.txt") as f:
    input = f.read().splitlines()

# Part 1
m = len(input)
M = [[int(input[i][j]) for j in range(m)] for i in range(m)]
cache = {}


def map_summits(i, j):
    if M[i][j] == 9:
        return {(i, j)}

    summits = set()
    for next_i, next_j in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        if (
            next_i >= 0
            and next_i < m
            and next_j >= 0
            and next_j < m
            and M[next_i][next_j] == M[i][j] + 1
        ):
            if (next_i, next_j) not in cache:
                cache[(next_i, next_j)] = map_summits(next_i, next_j)
            summits = summits.union(cache[(next_i, next_j)])

    return summits


res = 0
for i in range(m):
    for j in range(m):
        if M[i][j] == 0:
            res += len(map_summits(i, j))

print(res)


# Part 2, did this first accidentally lol
cache2 = {}


def score_trail(i, j):
    if M[i][j] == 9:
        return 1

    score = 0
    for next_i, next_j in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        if (
            next_i >= 0
            and next_i < m
            and next_j >= 0
            and next_j < m
            and M[next_i][next_j] == M[i][j] + 1
        ):
            if (next_i, next_j) not in cache2:
                cache2[(next_i, next_j)] = score_trail(next_i, next_j)
            score += cache2[(next_i, next_j)]

    return score


res2 = 0
for i in range(m):
    for j in range(m):
        if M[i][j] == 0:
            res2 += score_trail(i, j)

print(res2)
