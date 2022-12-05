from collections import defaultdict
import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/5/input.txt') as f:
    lines = f.read().splitlines()

# In input.txt, all lines trimmed down to relevant data separated by a single space

res = ''
stacks = defaultdict(list)

for line in lines[8:0:-1]:
    for i in range(0, 18, 2):
        if line[i] != ' ':
            stacks[i//2 + 1].append(line[i])

for line in lines[11:]:
    num, start, end = [int(x) for x in line.split(' ')]

    # Part 1
    # while num:
    #     stacks[end].append(stacks[start].pop())
    #     num -= 1

    # Part 2
    stacks[end].extend(stacks[start][-num:])
    while num:
        del stacks[start][-1]
        num -= 1

for stack in stacks.values():
    res += stack[-1]

print(res)
