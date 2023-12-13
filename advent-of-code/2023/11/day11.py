import os
from collections import defaultdict, deque, Counter


cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/11/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
G = lines.copy()
i = 0
while i < len(G):
    if all([c == "." for c in G[i]]):
        G.insert(i, G[i])
        i += 1
    i += 1

m = len(G)

j = 0
while j < len(G[0]):
    if all([G[x][j] == "." for x in range(m)]):
        for i in range(m):
            G[i] = G[i][:j] + "." + G[i][j:]
        j += 1
    j += 1

n = len(G[0])

# 148 x 145

galaxies = []
for i in range(m):
    for j in range(n):
        if G[i][j] == "#":
            galaxies.append((i, j))

res = 0
for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
        x1, y1, x2, y2 = galaxies[i][0], galaxies[i][1], galaxies[j][0], galaxies[j][1]
        res += abs(x1 - x2) + abs(y1 - y2)
print(res)

# Part 2
m, n = len(lines), len(lines[0])
expands = 0
for i in range(m):
    if lines[i] == "." * n:
        expands += 1
for j in range(n):
    if all([lines[x][j] == "." for x in range(m)]):
        expands += 1

galaxies = []
for i in range(m):
    for j in range(n):
        if lines[i][j] == "#":
            galaxies.append((i, j))

base = 0
for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
        x1, y1, x2, y2 = galaxies[i][0], galaxies[i][1], galaxies[j][0], galaxies[j][1]
        base += abs(x1 - x2) + abs(y1 - y2)

# 8860016, 9403026, 9946036
# diff of 543010
factor = 1_000_000
print(base + (factor - 1) * (res - base))
