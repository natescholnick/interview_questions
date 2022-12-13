import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/8/input.txt') as f:
    lines = f.read().splitlines()

trees = [[int(x) for x in line] for line in lines]
m, n = len(trees), len(trees[0])

# Part 1

visible = set()
for i in range(m):
    laneMax = -1
    for j in range(n):
        if trees[i][j] > laneMax:
            visible.add((i, j))
            laneMax = trees[i][j]

    laneMax = -1
    for j in range(n-1, -1, -1):
        if trees[i][j] > laneMax:
            visible.add((i, j))
            laneMax = trees[i][j]

for j in range(n):
    laneMax = -1
    for i in range(m):
        if trees[i][j] > laneMax:
            visible.add((i, j))
            laneMax = trees[i][j]

    laneMax = -1
    for i in range(m-1, -1, -1):
        if trees[i][j] > laneMax:
            visible.add((i, j))
            laneMax = trees[i][j]

print(len(visible))

# Part 2


def getScenicScore(x, y):
    n, e, s, w = 0, 0, 0, 0
    height = trees[x][y]
    for i in range(x-1, -1, -1):
        n += 1
        if trees[i][y] >= height:
            break
    for j in range(y+1, n):
        e += 1
        if trees[x][j] >= height:
            break
    for i in range(x+1, m):
        s += 1
        if trees[i][y] >= height:
            break
    for j in range(y-1, -1, -1):
        w += 1
        if trees[x][j] >= height:
            break
    return n*e*s*w


res = 0
for i in range(1, m-1):
    for j in range(1, n-1):
        res = max(res, getScenicScore(i, j))

print(res)
