import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/02/input.txt') as f:
    lines = f.read().splitlines()

# Part 1
result1 = 0
vals = {'X': 1, 'Y': 2, 'Z': 3}
for line in lines:
    result1 += vals[line[2]]
    if line in {'A X', 'B Y', 'C Z'}:
        result1 += 3
    if line in {'A Y', 'B Z', 'C X'}:
        result1 += 6

print(result1)

# Part 2
result2 = 0
vals = {'X': 0, 'Y': 3, 'Z': 6}
for line in lines:
    result2 += vals[line[2]]
    if line in {'A Y', 'B X', 'C Z'}:
        result2 += 1
    elif line in {'A Z', 'B Y', 'C X'}:
        result2 += 2
    else:
        result2 += 3

print(result2)
