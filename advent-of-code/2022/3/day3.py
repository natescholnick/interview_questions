import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/3/input.txt') as f:
    lines = f.read().splitlines()

# Part 1
result1 = 0
for line in lines:
    n = len(line)//2
    item = set(line[:n]).intersection(set(line[n:])).pop()
    if ord(item) < 97:
        result1 += ord(item) - 38
    else:
        result1 += ord(item) - 96

print(result1)

# Part 2
result2 = 0
for i in range(0, len(lines), 3):
    item = set(lines[i]).intersection(set(lines[i+1]), set(lines[i+2])).pop()
    if ord(item) < 97:
        result2 += ord(item) - 38
    else:
        result2 += ord(item) - 96

print(result2)
