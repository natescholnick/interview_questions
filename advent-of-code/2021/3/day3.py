from collections import defaultdict
import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2021/3/input.txt') as f:
    lines = f.read().splitlines()

# Part 1
n = len(lines[0])
sums = [0] * n
for line in lines:
    for i in range(n):
        sums[i] += int(line[i])

gamma = ''
for bits in sums:
    if bits > 500:
        gamma += '1'
    else:
        gamma += '0'
gamma = int(gamma, 2)
epsilon = 2**n - gamma - 1

print(gamma*epsilon)

# Part 2


def getRating(life):
    candidates = lines
    for i in range(n):
        ones = 0
        count = len(candidates)
        if count == 1:
            break
        for line in candidates:
            ones += int(line[i])
        candidates = list(filter(lambda x: int(x[i]) == life and ones >=
                                 count/2 or int(x[i]) != life and ones < count/2, candidates))
    return int(candidates[0], 2)


print(getRating(True) * getRating(False))
