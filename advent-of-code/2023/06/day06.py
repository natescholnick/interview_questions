import os
from functools import reduce

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/06/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
times = [int(x) for x in lines[0].split(" ")]
distances = [int(x) for x in lines[1].split(" ")]
n = len(times)
res = []

for i in range(n):
    charge = 0
    while charge * (times[i] - charge) <= distances[i]:
        charge += 1
    res.append(times[i] - 2 * charge + 1)

print(reduce(lambda x, y: x * y, res))

# Part 2
t = int(lines[0].replace(" ", ""))
d = int(lines[1].replace(" ", ""))
charge = 0
incrementer = 10000
while charge * (t - charge) <= d or incrementer > 1:
    if charge * (t - charge) > d:
        charge -= 0.9 * incrementer
        incrementer //= 10
    else:
        charge += incrementer
print(t - 2 * charge + 1)
