import os
from collections import deque

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/18/input.txt') as f:
    lines = f.read().splitlines()

input = set()
for line in lines:
    i, j, k = [int(a) for a in line.split(',')]
    input.add((i, j, k))

# Part 1
res = 0
for line in lines:
    i, j, k = [int(a) for a in line.split(',')]
    if (i+1, j, k) not in input:
        res += 1
    if (i-1, j, k) not in input:
        res += 1
    if (i, j+1, k) not in input:
        res += 1
    if (i, j-1, k) not in input:
        res += 1
    if (i, j, k+1) not in input:
        res += 1
    if (i, j, k-1) not in input:
        res += 1
print(res)


# Part 2
size = 0
for line in lines:
    i, j, k = [int(a) for a in line.split(',')]
    size = max(size, i, j, k)


def adjacentCells(i, j, k):
    return [(i+1, j, k), (i-1, j, k), (i, j+1, k), (i, j-1, k), (i, j, k+1), (i, j, k-1)]


def bfs(pt, seen):
    bubble = {pt}
    q = deque([pt])
    while q:
        i, j, k = q.popleft()
        for side in adjacentCells(i, j, k):
            if side in bubble:
                continue
            x, y, z = side
            if x == 0 or x >= size or y == 0 or y >= size or z == 0 or z >= size or side in seen:
                seen = seen.union(bubble)
                return True
            if side not in input:
                bubble.add(side)
                q.append(side)
    return False


res = 0
seen = set()
for point in input:
    for adj in adjacentCells(*point):
        if adj not in input and bfs(adj, seen):
            res += 1
print(res)
