import os
import heapq as hq

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/1/input.txt') as f:
    lines = f.readlines()

# # Part 1
# res = 0
# cur = 0
# for line in lines:
#     if line == '\n':
#         cur = 0
#         continue
#     cur += int(line)
#     res = max(res, cur)

# print(res)

# Part 2
three = []
cur = 0
for line in lines:
    if line == '\n':
        if len(three) < 3:
            hq.heappush(three, cur)
        else:
            hq.heappushpop(three, cur)
        cur = 0
        continue
    cur += int(line)

print(sum(three))