from collections import defaultdict
import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2021/05/input.txt') as f:
    lines = f.read().splitlines()

# Part 1
res = 0
M = [[0] * 1000 for _ in range(1000)]
for line in lines:
    x1, y1, x2, y2 = [int(x) for x in line.split(' ')]
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            M[x1][y] += 1
            if M[x1][y] == 2:
                res += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            M[x][y1] += 1
            if M[x][y1] == 2:
                res += 1
    # Part 2
    else:
        y = y1 if x1 < x2 else y2
        m = 1 if (x2-x1) * (y2-y1) > 0 else -1
        for x in range(min(x1, x2), max(x1, x2)+1):
            M[x][y] += 1
            if M[x][y] == 2:
                res += 1
            y += m
print(res)
