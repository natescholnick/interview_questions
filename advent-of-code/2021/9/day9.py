import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2021/9/input.txt') as f:
    lines = f.read().splitlines()

M = [[int(x) for x in line] for line in lines]

# Part 1
res = 0
basins = {}
m, n = len(M), len(M[0])
for i in range(m):
    for j in range(n):
        if (i == 0 or M[i][j] < M[i-1][j]) and (i == m-1 or M[i][j] < M[i+1][j]) and (j == 0 or M[i][j] < M[i][j-1]) and (j == n-1 or M[i][j] < M[i][j+1]):
            res += M[i][j] + 1
            basins[(i, j)] = 0
print(res)

# Part 2
seen = set()


def dfs(i, j, basin, prev):
    if i < 0 or j < 0 or i >= m or j >= n or M[i][j] == 9 or M[i][j] <= prev or (i, j) in seen:
        return
    seen.add((i, j))
    basins[basin] += 1
    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        dfs(x, y, basin, M[i][j])


for x, y in basins:
    dfs(x, y, (x, y), -1)

res2 = 1
for size in sorted(basins.values(), reverse=True)[:3]:
    res2 *= size

print(res2)
