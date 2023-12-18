import os
from collections import defaultdict, deque, Counter
import re
import heapq

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/18/input.txt") as f:
    lines = f.read().splitlines()


# Part 1
i0 = j0 = i1 = j1 = 0
currI = currJ = 0
for line in lines:
    dir, dist, _ = line.split(' ')
    dist = int(dist)
    if dir == 'L':
        currJ -= dist
    if dir == 'R':
        currJ += dist
    if dir == 'U':
        currI -= dist
    if dir == 'D':
        currI += dist
    i0 = min(i0, currI)
    i1 = max(i1, currI)
    j0 = min(j0, currJ)
    j1 = max(j1, currJ)

# If starting hole is 0, 0, the bounding box is
# i: [-352, 13], j: [-194, 230]

m, n = i1 - i0 + 1, j1 - j0 + 1
G = [['.' for _ in range(n)] for _ in range(m)]
i, j = -i0, -j0
G[i][j] = '#'
dirs = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}
for line in lines:
    dir, dist, _ = line.split(' ')
    dist = int(dist)
    di, dj = dirs[dir]
    for _ in range(dist):
        i += di
        j += dj
        G[i][j] = '#'


seen = set()
q = []

for j in range(n):
    q.append((0, j))
    q.append((m-1, j))
for i in range(1, m-1):
    q.append((i, 0))
    q.append((i, n-1))

while q:
    i, j  = q.pop()
    if i < 0 or i >= m or j < 0 or j >= n or (i, j) in seen or G[i][j] == '#':
        continue
    seen.add((i, j))
    q.extend([(i+1, j), (i-1, j), (i, j+1), (i, j-1)])

print(m*n - len(seen))

# Part 2
