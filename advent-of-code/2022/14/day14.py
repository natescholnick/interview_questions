from collections import Counter
import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/14/input.txt') as f:
    lines = f.read().splitlines()

n = len(lines)
x_max, y_min, y_max = 0, 500, 0

for line in lines:
    coords = line.split(' ')
    for coord in coords:
        y, x = [int(a) for a in coord.split(',')]
        x_max = max(x_max, x)
        y_min = min(y_min, y)
        y_max = max(y_max, y)

# Part 2, bounding maximal sand pyramid  #
x_max += 1  # 174                        #
y_min, y_max = 500 - x_max, 500 + x_max  #
##########################################

M = [['.' for _ in range(y_max - y_min + 1)] for _ in range(x_max + 1)]
start = 500 - y_min


# Make cave
for line in lines:
    prev_x = None
    coords = line.split(' ')
    for coord in coords:
        if prev_x == None:
            prev_y, prev_x = [int(a) for a in coord.split(',')]
            prev_y -= y_min
            continue
        y, x = [int(x) for x in coord.split(',')]
        y -= y_min
        if x == prev_x:
            low, high = min(y, prev_y), max(y, prev_y)
            for j in range(low, high + 1):
                M[x][j] = '#'
        else:
            low, high = min(x, prev_x), max(x, prev_x)
            for i in range(low, high + 1):
                high
                M[i][y] = '#'
        prev_x, prev_y = x, y

# # Part 1
# def drop(x, y):   # True if sand comes to rest
#     if x == x_max:
#         return False
#     if M[x+1][y] == '.':
#         return drop(x+1, y)
#     elif y == 0:
#         return False
#     elif M[x+1][y-1] == '.':
#         return drop(x+1, y-1)
#     elif y == len(M[0]) - 1:
#         return False
#     elif M[x+1][y+1] == '.':
#         return drop(x+1, y+1)
#     else:
#         M[x][y] = 'o'
#         return True

# res = -1
# rest = True
# while rest:
#     rest = drop(0, start)
#     res += 1

# print(res)

# Part 2


def drop(x, y):  # True once blocked
    if x == x_max:
        M[x][y] = 'o'
        return False
    if M[x+1][y] == '.':
        drop(x+1, y)
    elif M[x+1][y-1] == '.':
        drop(x+1, y-1)
    elif M[x+1][y+1] == '.':
        drop(x+1, y+1)
    else:
        M[x][y] = 'o'
        if (x, y) == (0, start):
            return True
    return False


res = 0
blocked = False
while not blocked:
    res += 1
    blocked = drop(0, start)

print(res)
