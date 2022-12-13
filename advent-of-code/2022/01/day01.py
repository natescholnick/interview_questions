import os
import heapq as hq

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/1/input.txt') as f:
    lines = f.readlines()

# # Part 1
result1 = 0
running_sum = 0
for line in lines:
    if line == '\n':
        running_sum = 0
        continue
    running_sum += int(line)
    result1 = max(result1, running_sum)

print(result1)

# Part 2
top_three = []
running_sum = 0
for line in lines:
    if line == '\n':
        if len(top_three) < 3:
            hq.heappush(top_three, running_sum)
        else:
            hq.heappushpop(top_three, running_sum)
        running_sum = 0
        continue
    running_sum += int(line)

print(sum(top_three))
