import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/4/input.txt') as f:
    lines = f.read().splitlines()

# Note that I altered the input, replacing all punctuation with empty spaces

# Part 1
result1 = 0
for line in lines:
    x1, y1, x2, y2 = [int(x) for x in line.split(' ')]

    if x1 <= x2 and y1 >= y2 or x2 <= x1 and y2 >= y1:
        result1 += 1

print(result1)


# Part 2
result2 = 0
for line in lines:
    x1, y1, x2, y2 = [int(x) for x in line.split(' ')]

    if x1 <= x2 and y1 >= x2 or x2 <= x1 and y2 >= x1:
        result2 += 1

print(result2)
