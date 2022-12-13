from collections import deque
import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/12/input.txt') as f:
    lines = f.read().splitlines()

M = [[ord(c) for c in line] for line in lines]
m, n = len(M), len(M[0])

# # Part 1
# for i in range(m):
#     for j in range(n):
#         if M[i][j] == 69:
#             end = (i, j)
#             M[i][j] = ord('z')

# q = deque([])
# q.append((20, 0, 0))
# seen = {(20, 0)}
# while q:
#     x, y, steps = q.popleft()
#     if (x, y) == end:
#         res = steps
#         break
#     for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
#         if i >= 0 and i < m and j >= 0 and j < n and (i, j) not in seen and M[i][j] <= M[x][y] + 1:
#             seen.add((i, j))
#             q.append((i, j, steps + 1))

# print(res)


# Part 2 (exact same thing, just start from the end)

q = deque([])
q.append((20, 72, 0))  # end coordinates from Part 1
seen = {(20, 72)}
while q:
    x, y, steps = q.popleft()
    if M[x][y] == ord('a'):
        res = steps
        break
    for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if i >= 0 and i < m and j >= 0 and j < n and (i, j) not in seen and M[i][j] >= M[x][y] - 1:
            seen.add((i, j))
            q.append((i, j, steps + 1))

print(res)
