import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2023/02/input.txt') as f:
    lines = f.readlines()

# Part 1
maxes = {'r': 12, 'g': 13, 'b': 14}
res = 0
for i in range(len(lines)):
    possible = True
    games = lines[i].split()
    for j in range(0, len(games), 2):
        num, color = int(games[j]), games[j + 1]
        if maxes[color] < num:
            possible = False
            break
    if possible:
        res += i + 1


print(res)

# Part 2
res2 = 0
for i in range(len(lines)):
    games = lines[i].split()
    mins = {'r': 0, 'g': 0, 'b': 0}
    for j in range(0, len(games), 2):
        num, color = int(games[j]), games[j + 1]
        mins[color] = max(mins[color], num)
    res2 += mins['r'] * mins['g'] * mins['b']
print(res2)