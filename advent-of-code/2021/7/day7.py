from collections import Counter
import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2021/7/input.txt') as f:
    data = f.read().split(',')

data = [int(x) for x in data]
data.sort()
n = len(data)

# Part 1
res = 0
M = data[n//2]
for x in data:
    res += abs(M - x)
print(res)

# Part 2


def getCost(x):
    fuel = 0
    for x_i in data:
        dist = abs(x - x_i)
        fuel += dist * (dist + 1) // 2
    return fuel


cost = getCost(M)
while True:
    cost_down = getCost(M - 1)
    if cost_down < cost:
        M -= 1
        cost = cost_down
        continue
    cost_up = getCost(M + 1)
    if cost_up < cost:
        M += 1
        cost = cost_up
        continue
    break

print(cost)
