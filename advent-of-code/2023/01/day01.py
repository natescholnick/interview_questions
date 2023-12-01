import os
import heapq as hq

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2023/01/input.txt') as f:
    lines = f.readlines()

# # Part 1
res = 0
for line in lines:
    for c in line:
        if c.isdigit():
            res += 10 * int(c)
            break
    for c in line[::-1]:
        if c.isdigit():
            res += int(c)
            break

print(res)

# Part 2
res2 = 0
digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for line in lines:
    num = 0
    for i in range(len(line)):
        if line[i].isdigit():
            num += 10 * int(line[i])
            break
        for d in range(len(digits)):
            if line[i:i+len(digits[d])] == digits[d]:
                num += 10 * (d+1)
                break
        if num > 0:
            break
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            num += int(line[i])
            break
        for d in range(len(digits)):
            if line[i-len(digits[d]):i] == digits[d]:
                num += d + 1
                break
        if num % 10:
            break
    res2 += num

print(res2)