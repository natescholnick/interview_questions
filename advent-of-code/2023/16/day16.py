import os
from collections import defaultdict, deque, Counter
import re

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/16/input.txt") as f:
    G = f.read().splitlines()


# Part 1
m, n = len(G), len(G[0])
directions = {
    'l': (0, -1),
    'r': (0, 1),
    'u': (-1, 0),
    'd': (1, 0),
}
bounces = {
    '.': {'l': 'l',
          'r': 'r',
          'u': 'u',
          'd': 'd'},
    '/': {'l': 'd',
          'r': 'u',
          'u': 'r',
          'd': 'l'},
    '\\': {'l': 'u',
          'r': 'd',
          'u': 'l',
          'd': 'r'},
    '|': {'l': ('u', 'd'),
          'r': ('u', 'd'),
          'u': 'u',
          'd': 'd'},
    '-': {'l': 'l',
          'r': 'r',
          'u': ('l', 'r'),
          'd': ('l', 'r')},
}

seen = defaultdict(set)

def followDir(i, j, dir):
    if i < 0 or i >= m or j < 0 or j >= n or dir in seen[(i, j)]:
        return
    seen[(i, j)].add(dir)
    newDir = bounces[G[i][j]][dir]
    if isinstance(newDir, tuple):
        q.append((i, j, newDir[1]))
        newDir = newDir[0]
    di, dj = directions[newDir]
    followDir(i + di, j + dj, newDir)
        

q = []
q.append((0, 0, 'r'))
while q:
    i, j, dir = q.pop()
    followDir(i, j, dir)

print(len(seen))

# Part 2
res2 = 0
for y in range(m):
    seen = defaultdict(set)
    q = [(y, 0, 'r')]
    while q:
        i, j, dir = q.pop()
        followDir(i, j, dir)
    res2 = max(res2, len(seen))

    seen = defaultdict(set)
    q = [(y, n-1, 'l')]
    while q:
        i, j, dir = q.pop()
        followDir(i, j, dir)

    res2 = max(res2, len(seen))

for x in range(n):
    seen = defaultdict(set)
    q = [(0, x, 'd')]
    while q:
        i, j, dir = q.pop()
        followDir(i, j, dir)
    res2 = max(res2, len(seen))

    seen = defaultdict(set)
    q = [(m-1, x, 'u')]
    while q:
        i, j, dir = q.pop()
        followDir(i, j, dir)

    res2 = max(res2, len(seen))
print(res2)

