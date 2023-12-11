import os
from collections import defaultdict
from collections import Counter
from collections import deque

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/10/input.txt") as f:
    lines = f.read().splitlines()

m, n = len(lines), len(lines[0])
for i in range(m):
    lines[i] = [*lines[i]]

# Part 1
tileToAdj = {
    "-": ((0, 1), (0, -1)),
    "|": ((1, 0), (-1, 0)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((1, 0), (0, -1)),
    "F": ((1, 0), (0, 1)),
}
# keys must be sorted
AdjToTile = {
    ((0, -1), (0, 1)): "-",
    ((-1, 0), (1, 0)): "|",
    ((-1, 0), (0, 1)): "L",
    ((-1, 0), (0, -1)): "J",
    ((0, -1), (1, 0)): "7",
    ((0, 1), (1, 0)): "F",
}
loopLength = 1
seen = set()

for i in range(m):
    for j in range(n):
        if lines[i][j] == "S":
            si, sj = i, j
            seen.add((si, sj))
            break
# 41, 111

sAdj = []
for adj in sorted([(1, 0), (-1, 0), (0, 1), (0, -1)]):
    if (-adj[0], -adj[1]) in tileToAdj[lines[si + adj[0]][sj + adj[1]]]:
        sAdj.append(adj)

lines[si][sj] = AdjToTile[tuple(sAdj)]
i, j = si + sAdj[0][0], sj + sAdj[0][1]
# 40, 111


def takeStep(i, j):
    opt1, opt2 = tileToAdj[lines[i][j]]
    if (i + opt1[0], j + opt1[1]) not in seen:
        return i + opt1[0], j + opt1[1]
    else:
        return i + opt2[0], j + opt2[1]


while (i, j) not in seen:
    seen.add((i, j))
    i, j = takeStep(i, j)
    loopLength += 1

print(loopLength // 2)

# Part 2
isLoop = seen.copy()
seen = set()
res = 0
tileToSides = {
    "-": ([(1, 0)], [(-1, 0)]),
    "|": ([(0, 1)], [(0, -1)]),
    "L": ([(-1, 0), (0, 1)], [(1, 0), (0, -1)]),
    "7": ([(-1, 0), (0, 1)], [(1, 0), (0, -1)]),
    "J": ([(-1, 0), (0, -1)], [(1, 0), (0, 1)]),
    "F": ([(-1, 0), (0, -1)], [(1, 0), (0, 1)]),
}


def dfs(i, j):
    if (i, j) in isLoop or lines[i][j] == "I":
        return
    global res
    res += 1
    lines[i][j] = "I"
    for next in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        dfs(*next)


# compute the interior direction of the current tile based on the previous
def incrementInside(i, j, insideVector):
    opt1, opt2 = tileToSides[lines[i][j]]
    return opt1 if insideVector in opt1 else opt2


for row in range(m):
    if len(seen) > 0:
        break
    for col in range(n):
        if (row, col) in isLoop:
            seen = set((row, col))
            prev = (row, col)
            inside = ((1, 0), (0, 1))
            i, j = row, col + 1
            break


for _ in range(loopLength - 2):
    # There are 1 or 2 inward pointing vectors, but we only consider the one perpendicular to the connection
    # To wit: if two tiles are connected horizontally, it is their vertical vector that must match
    if i == prev[0]:
        vector = [v for v in inside if v[1] == 0][0]
    else:
        vector = [v for v in inside if v[0] == 0][0]
    prev = (i, j)

    inside = incrementInside(i, j, vector)

    for k in range(len(inside)):
        dfs(i + list(inside)[k][0], j + list(inside)[k][1])

    # step to next tile, as in part 1
    seen.add((i, j))
    i, j = takeStep(i, j)


print(res)
