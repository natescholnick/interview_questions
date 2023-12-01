import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2021/02/input.txt') as f:
    lines = f.read().splitlines()

# Part 1
# f, d = 0, 0
# for line in lines:
#     direction, distance = line.split(' ')
#     x = int(distance)
#     if direction == 'f':
#         f += x
#     elif direction == 'd':
#         d += x
#     else:
#         d -= x
# print(f*d)

# Part 2
f, d, a = 0, 0, 0
for line in lines:
    direction, distance = line.split(' ')
    x = int(distance)
    if direction == 'f':
        f += x
        d += a * x
    elif direction == 'd':
        a += x
    else:
        a -= x
print(f*d)
