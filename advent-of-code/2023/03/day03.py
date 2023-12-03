import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2023/03/input.txt') as f:
    lines = f.read().splitlines()

# Part 1
def verify(i, j):
    num = 0
    _j = j
    skip = set()
    while _j < len(lines[i]) and lines[i][_j].isdigit():
         skip.add((i, _j))
         num = 10 * num + int(lines[i][_j])
         _j += 1

    for x in range(i - 1, i + 2):
        for y in range(j - 1, _j + 1):
            if x < 0 or y < 0 or x >= len(lines) or y >= len(lines[i]) or (x, y) in skip:
                continue
            if lines[x][y] != '.':
                return num
    return 0


res = 0
for i in range(len(lines)):
    read = True
    for j in (range(len(lines[i]))):
        d = lines[i][j]
        if read and d.isdigit():
            res += verify(i, j)
            read = False
        elif not d.isdigit():
            read = True

print(res)

# Part 2
def findNum(i, j):
    lj, rj = j, j
    while lj >= 0 and lines[i][lj].isdigit():
        lj -= 1
    lj += 1
    while rj < len(lines[i]) and lines[i][rj].isdigit():
        rj += 1
    return int(lines[i][lj:rj]), {(i, lj + d) for d in range(rj-lj)}

def gearCheck(i, j):
    skip = {(i, j)}
    adj = []
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x < 0 or y < 0 or x >= len(lines) or y >= len(lines[i]) or (x, y) in skip:
                continue
            if lines[x][y].isdigit():
                num, cells = findNum(x, y)
                adj.append(num)
                skip = skip.union(cells)
    if len(adj) == 2:
        return adj[0] * adj[1]
    return 0


res2 = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '*':
            res2 += gearCheck(i, j)
print(res2)