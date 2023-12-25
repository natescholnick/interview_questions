import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

file = 'input'
with open(f"{cwd}/advent-of-code/2023/24/{file}.txt") as f:
    lines = f.read().splitlines()


# Part 1
res = 0
stones = []
b = (7, 27) if file == 'example' else (200000000000000, 400000000000000)
for line in lines:
    x0, y0, z0, vx0, vy0, vz0 = (int(x) for x in line.split(' '))
    p0 = (x0, y0, z0)
    v0 = (vx0, vy0, vz0)
    for stone in stones:
        p1, v1 = stone
        x1, y1, z1 = p1
        # parallel
        if v0[1]/v0[0] == v1[1]/v1[0]:
            continue
        t1 = (y0 - y1 + v0[1] * (x1 - x0) / v0[0]) / (v1[1] - v0[1] * v1[0] / v0[0])
        if t1 <= 0:
            continue
        t0 = (x1 - x0 + t1*v1[0]) / v0[0]
        if t0 <= 0:
            continue
        res += b[0] <= x0 + t0 * v0[0] <= b[1] and b[0] <= y0 + t0 * v0[1] <= b[1]

    stones.append((p0, v0))

print(res)

# Part 2
# # An elegant solution isn't occurring to me, but I think this will work:
# # Consider every vector as a potential t=2... collision
# # From there, consider all possible second collisions as time decrements
# # With a second collision selected, the vector is defined and can be evaluated


# # This code works for the example, but has no chance with the full input
# def collides(a, b):
#     pa, va = a
#     pb, vb = b
#     times = []
#     for i in range(3):
#         if va[i] == vb[i]:
#             if pa[i] != pb[i]:
#                 return False
#         else:
#             times.append((pa[i] - pb[i]) / (vb[i] - va[i]))
#     # must be a future collision
#     if times[0] < 0:
#         return False
#     return all([t == times[0] for t in times])

# t2 = 2
# res = None
# while not res:
#     print(t2)
#     for stone2 in stones:
#         p2x, p2y, p2z = stone2[0][0] + t2 * stone2[1][0], stone2[0][1] + t2 * stone2[1][1], stone2[0][2] + t2 * stone2[1][2]
#         for t1 in range(t2-1, 0, -1):
#             for stone1 in stones:
#                 if stone1 == stone2:
#                     continue
#                 p1x, p1y, p1z = stone1[0][0] + t1 * stone1[1][0], stone1[0][1] + t1 * stone1[1][1], stone1[0][2] + t1 * stone1[1][2]
#                 v = [(p2x - p1x) / (t2 - t1), (p2y - p1y) / (t2 - t1), (p2z - p1z) / (t2 - t1)]
#                 if not all([_v.is_integer() for _v in v]):
#                     continue
#                 v = tuple(int(_v) for _v in v)
#                 p0 = [p1x - t1 * v[0], p1y - t1 * v[1], p1z - t1 * v[2]]
#                 res = sum(p0)
#                 for stone in stones:
#                     if not collides(stone, (p0, v)):
#                         res = None
#                         break
#                 if res: break
#             if res: break
#         if res: break
#     t2 += 1
# print(res)
# print(p0, v)

# # As my code runs on, I know I'll need to come up with something faster.
# # Let's try to compare stones that appear to be converging
# def dist(a, b, t):
#     return math.sqrt((a[0][0] + t * a[1][0] - (b[0][0] + t * b[1][0]))**2 + (a[0][1] + t * a[1][1] - (b[0][1] + t * b[1][1]))**2 + (a[0][2] + t * a[1][2] - (b[0][2] + t * b[1][2]))**2)

# # Differentiated two vectors' distance equation in 3-space and solved for t:
# # x_1(t) = at + b  |  x_2(t) = gt + h
# # y_1(t) = ct + d  |  y_2(t) = it + j
# # z_1(t) = et + f  |  z_2(t) = kt + l
# def findNearestMoment(v1, v2):
#     a, b, c, d, e, f = v1[1][0], v1[0][0], v1[1][1], v1[0][1], v1[1][2], v1[0][2]
#     g, h, i, j, k, l = v2[1][0], v2[0][0], v2[1][1], v2[0][1], v2[1][2], v2[0][2]
#     return int(-((a-g)*(b-h) + (c-i)*(d-j) + (e-k)*(f-l))/((a-g)**2 + (c-i)**2 + (e-k)**2))

# # Well, think what you will future me, this mess ^ appears to work
# # Using this utility, let's find the three closest encounters for each hailstorm
# m = len(stones)
# nearest = [[] for _ in range(m)]
# for i in range(m-1):
#     for j in range(i+1, m):
#         if stones[i] == stones[j]:
#             continue
#         t = findNearestMoment(stones[i], stones[j])
#         d = dist(stones[i], stones[j], t)
#         bisect.insort(nearest[i], (d, t, j))
#         if len(nearest[i]) > 3:
#             nearest[i].pop()
#         bisect.insort(nearest[j], (d, t, i))
#         if len(nearest[j]) > 3:
#             nearest[j].pop()

# avg = sum([x[0] for x in nearest[0]])
# candidate = 0
# for i in range(m):
#     distSum = sum([x[0] for x in nearest[i]])
#     if distSum < avg:
#         candidate = i
#         avg = distSum

# print(candidate) # 151
# print(nearest[candidate]) # 215, 150, 61

# # The prospective time range is still way to big, ~3_000_000_000

# Too long coding, I'm not gonna come up with a new approach.
# Just gonna see about building a system of equations and plug it into numpy
coefficients = []
constants = []
res = []
resV = [] # not strictly necessary, but nice for verification
for i in range(4):
    p, v = stones[i]
    p0, v0 = stones[i+1]
    coefficients.append([v0[1]-v[1], p[1]-p0[1], v[0]-v0[0], p0[0]-p[0]])
    constants.append(p0[0]*v0[1] - p0[1]*v0[0] - p[0]*v[1] + p[1]*v[0])

a = np.array(coefficients, dtype=np.int64)
b = np.array(constants, dtype=np.int64)
XandY = np.linalg.solve(a, b)

res.append(int(XandY[0]))
res.append(int(XandY[2]))
resV.append(int(XandY[1]))
resV.append(int(XandY[3]))


coefficients = []
constants = []
for i in range(4, 8):
    p, v = stones[i]
    p0, v0 = stones[i+1]
    coefficients.append([v0[2]-v[2], p[2]-p0[2], v[0]-v0[0], p0[0]-p[0]])
    constants.append(p0[0]*v0[2] - p0[2]*v0[0] - p[0]*v[2] + p[2]*v[0])

c = np.array(coefficients, dtype=np.int64)
d = np.array(constants, dtype=np.int64)
XandZ = np.linalg.solve(c, d)
res.append(int(XandZ[2]))
resV.append(int(XandZ[3]))

print(res)
print(resV)
print(sum(res))
# I'm so disappointed this is the effort to do it...

