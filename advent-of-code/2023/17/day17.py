import os
from collections import defaultdict, deque, Counter
import re
import heapq

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/17/input.txt") as f:
    G = f.read().splitlines()


# Part 1
m, n = len(G), len(G[0])
def nextState(i, j, streak):
    next = []
    if streak[0]:
        next.append((i, j+1, (0, 1)))
        next.append((i, j-1, (0, -1)))
        if streak[0] > 0 and streak[0] < 3:
            next.append((i+1, j, (streak[0] + 1, 0)))
        elif streak[0] < 0 and streak[0] > -3:
            next.append((i-1, j, (streak[0] - 1, 0)))
    else:
        next.append((i+1, j, (1, 0)))
        next.append((i-1, j, (-1, 0)))
        if streak[1] > 0 and streak[1] < 3:
            next.append((i, j+1, (0, streak[1] + 1)))
        elif streak[1] < 0 and streak[1] > -3:
            next.append((i, j-1, (0, streak[1] - 1)))
    return next

res = float('inf')
seen = defaultdict(lambda: float("inf"))
seen[(0, 1, (0, 1))] = 0
seen[(1, 0, (1, 0))] = 0
q = []
heapq.heappush(q, (0, 0, 1, (0, 1)))
heapq.heappush(q, (0, 1, 0, (1, 0)))
while q:
    pathSum, i, j, streak = heapq.heappop(q)
    if i < 0 or i >= m or j < 0 or j >= n:
        continue
    pathSum += int(G[i][j])
    if i == m-1 and j == n-1:
        res = min(res, pathSum)
        continue
    for ni, nj, ns in nextState(i, j, streak):
        if pathSum < seen[(ni, nj, ns)] and pathSum < res:
            seen[(ni, nj, ns)] = pathSum
            heapq.heappush(q, (pathSum, ni, nj, ns))

print(res)

# Part 2
def nextState2(i, j, streak):
    next = []
    if streak[0]:
        if abs(streak[0]) > 3:
            next.append((i, j+1, (0, 1)))
            next.append((i, j-1, (0, -1)))
        if streak[0] > 0 and streak[0] < 10:
            next.append((i+1, j, (streak[0] + 1, 0)))
        elif streak[0] < 0 and streak[0] > -10:
            next.append((i-1, j, (streak[0] - 1, 0)))
    else:
        if abs(streak[1]) > 3:
            next.append((i+1, j, (1, 0)))
            next.append((i-1, j, (-1, 0)))
        if streak[1] > 0 and streak[1] < 10:
            next.append((i, j+1, (0, streak[1] + 1)))
        elif streak[1] < 0 and streak[1] > -10:
            next.append((i, j-1, (0, streak[1] - 1)))
    return next

res2 = float('inf')
seen = defaultdict(lambda: float("inf"))
seen[(0, 1, (0, 1))] = 0
seen[(1, 0, (1, 0))] = 0
heapq.heappush(q, (0, 0, 1, (0, 1)))
heapq.heappush(q, (0, 1, 0, (1, 0)))
while q:
    pathSum, i, j, streak = heapq.heappop(q)
    if i < 0 or i >= m or j < 0 or j >= n:
        continue
    pathSum += int(G[i][j])
    if i == m-1 and j == n-1:
        res2 = min(res2, pathSum)
        continue
    for ni, nj, ns in nextState2(i, j, streak):
        if pathSum < seen[(ni, nj, ns)] and pathSum < res2:
            seen[(ni, nj, ns)] = pathSum
            heapq.heappush(q, (pathSum, ni, nj, ns))

print(res2)

