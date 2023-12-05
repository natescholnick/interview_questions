import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2021/01/input.txt') as f:
    lines = f.readlines()

# # Part 1
# res = 0
# for i in range(1, len(lines)):
#     if lines[i] > lines[i-1]:
#         res += 1

# Part 2
res = 0
for i in range(3, len(lines)):
    if lines[i] > lines[i-3]:
        res += 1

print(res)