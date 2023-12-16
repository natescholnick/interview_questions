import os
from collections import defaultdict, deque, Counter
import re

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/14/input.txt") as f:
    G = f.read().splitlines()

# Part 1
res = 0
m, n = len(G), len(G[0])
for col in range(n):
    weight = n
    for row in range(m):
        if G[row][col] == 'O':
            res += weight
            weight -= 1
        elif G[row][col] == '#':
            weight = n - row - 1
print(res)

# Part 2
def rollRight(grid):
    for i in range(m):
        newRow = []
        rocks = 0
        for j in range(n):
            if grid[i][j] == 'O':
                rocks += 1
            elif grid[i][j] == '.':
                newRow.append('.')
            else:
                newRow.extend(rocks * ['O'] + ['#'])
                rocks = 0
        newRow.extend(rocks * ['O'])
        grid[i] = ''.join(newRow)
    return grid

def spin(grid, x):
    for _ in range(x):
        for _ in range(4):
            grid = list(zip(*grid[::-1]))
            grid = rollRight(grid)
    return grid


# prev = spin(G, 499)
# G = spin(prev, 1)

# coords = {0: set(),
#           1: set(),
#           2: set(),
#           3: set()}

# for _ in range(100):
#     diff = []
#     for i in range(m):
#         for j in range(n):
#             if G[i][j] != prev[i][j]:
#                 diff.append((i, j))
#     print(diff)
#     for i, coord in enumerate(diff):
#         coords[i].add(coord)

#     prev = G
#     G = spin(G, 1)

# for k, v in coords.items():
#     print(k, len(v))

# the pattern in modulo 42, starting sometime before 500 spins
# print(999999500 % 42) = 38

G = spin(G, 538)
res2 = 0
for i in range(m):
    for j in range(n):
        if G[i][j] == 'O':
            res2 += m - i
print(res2)