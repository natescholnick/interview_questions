from collections import Counter
import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2021/06/input.txt') as f:
    fish = f.read()

# Part 1
fish = [int(x) for x in fish.split(' ')]

d = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
memo = [1]
# Part 2, use range(255)
for i in range(79):
    new = d[0]
    for x in range(8):
        d[x] = d[x+1]
    d[8] = new
    d[6] += new
    memo.append(sum(d.values()))

res = 0
for k, v in Counter(fish).items():
    res += v * memo[-k]
print(res)
