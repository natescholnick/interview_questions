import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/09/input.txt') as f:
    lines = f.read().splitlines()


def updateTail(x1, y1, x2, y2):
    # tail doesn't move
    if abs(x1-x2) < 2 and abs(y1-y2) < 2:
        return [x2, y2]
    # tail moves up or down
    if x1 == x2:
        if y1 > y2:
            return [x2, y2 + 1]
        return [x2, y2 - 1]
    # tail moves left or right
    if y1 == y2:
        if x1 > x2:
            return [x2 + 1, y2]
        return [x2 - 1, y2]
    # diagonal cases
    if x1 > x2 and y1 > y2:
        return [x2 + 1, y2 + 1]
    if x1 > x2 and y1 < y2:
        return [x2 + 1, y2 - 1]
    if x1 < x2 and y1 > y2:
        return [x2 - 1, y2 + 1]
    if x1 < x2 and y1 < y2:
        return [x2 - 1, y2 - 1]


# Part 1
coords = set()
x1, y1, x2, y2 = 0, 0, 0, 0
for line in lines:
    direction, distance = line.split(' ')
    distance = int(distance)
    while distance > 0:
        if direction == 'U':
            y1 += 1
        elif direction == 'R':
            x1 += 1
        elif direction == 'D':
            y1 -= 1
        else:
            x1 -= 1
        x2, y2 = updateTail(x1, y1, x2, y2)
        coords.add((x2, y2))
        distance -= 1

print(len(coords))

# Part 2
coords2 = set()
knots = [[0, 0] for _ in range(10)]
for line in lines:
    direction, distance = line.split(' ')
    distance = int(distance)
    while distance > 0:
        if direction == 'U':
            knots[0][1] += 1
        elif direction == 'R':
            knots[0][0] += 1
        elif direction == 'D':
            knots[0][1] -= 1
        else:
            knots[0][0] -= 1
        for i in range(1, 10):
            x2, y2 = updateTail(
                knots[i-1][0], knots[i-1][1], knots[i][0], knots[i][1])
            if x2 == knots[i][0] and y2 == knots[i][1]:
                break
            knots[i] = [x2, y2]
        coords2.add(tuple(knots[-1]))
        distance -= 1

print(len(coords2))
