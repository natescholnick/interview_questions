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
# Time for something I learned earlier this AoC: Shoelace formula!

# The directions connect 1x1 squares, not points, which adds a layer of difficulty
# All points must be pushes half units from their cell's center to its exterior corner
# points[-1] = (0, 1) # increases area
# points[-1] = (-1, 0) # increases area
# Therefore, the interior is down and right from the origin
def calcExterior(dir1, dir2, ext):
    if dir1 in {'R', 'L'}:
        if ext[1] > 0:
            if dir2 == 'U':
                ext[0] = -0.5
            else:
                ext[0] = 0.5
        else:
            if dir2 == 'U':
                ext[0] = 0.5
            else:
                ext[0] = -0.5
    if dir1 == 'L':
        ext[0] *= -1
    if dir1 in {'U', 'D'}:
        if ext[0] > 0:
            if dir2 == 'R':
                ext[1] = -0.5
            else:
                ext[1] = 0.5
        else:
            if dir2 == 'R':
                ext[1] = 0.5
            else:
                ext[1] = -0.5
    if dir1 == 'D':
        ext[1] *= -1
    return ext


points = []
curr = [0, 0]
out = [-0.5, 0]
prev = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}[lines[-1].split(' ')[2][-1]]
for line in lines:
    _, __, code = line.split(' ')
    dir = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}[code[-1]]
    dist = int(code[:5], 16)
    out = calcExterior(prev, dir, out)
    prev = dir
    points.append((curr[0] + out[0], curr[1] + out[1]))
    if dir == 'L':
        curr[0] -= dist
    if dir == 'R':
        curr[0] += dist
    if dir == 'U':
        curr[1] += dist
    if dir == 'D':
        curr[1] -= dist

area = 0
for i in range(len(points)):
    area += int(points[i-1][1] + points[i][1]) * int(points[i-1][0] - points[i][0])

print(abs(area) // 2)