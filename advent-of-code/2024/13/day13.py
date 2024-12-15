import os
import sys
from collections import defaultdict, deque, Counter, namedtuple
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/13/input.txt") as f:
    lines = f.read().splitlines()

V = namedtuple("V", ["x", "y"])


def process_line(line, part2=False):
    xy = line.split(": ")[1]
    x, y = xy.split(", ")
    x = int(x[2:])
    y = int(y[2:])
    if part2:
        x += 10000000000000
        y += 10000000000000
    return V(x, y)


def process_input(i, part2=False):
    A = process_line(lines[i])
    B = process_line(lines[i + 1])
    P = process_line(lines[i + 2], part2)
    return A, B, P


# Part 1
res = 0
for i in range(0, len(lines), 4):
    A, B, P = process_input(i)
    # P is not in the span of A and B
    if (A.y / A.x > P.y / P.x and B.y / B.x > P.y / P.x) or (
        A.y / A.x < P.y / P.x and B.y / B.x < P.y / P.x
    ):
        continue
    a = x = y = 0
    # within bounds and waiting for our difference to be a multiple of B
    while (
        x < P.x
        and y < P.y
        and a < 100
        and (
            (P.x - x) % B.x != 0
            or (P.y - y) % B.y != 0
            or (P.x - x) // B.x != (P.y - y) // B.y
            or (P.x - x) // B.x > 100
        )
    ):
        a += 1
        x += A.x
        y += A.y
    if x < P.x and y < P.y and a < 100:
        res += 3 * a + (P.x - x) // B.x

print(res)


# Part 2
# A and B are always linearly independent
# Always one of each: slope > 1, slope < 1
def extended_gcd(x, y):
    if y == 0:
        return x, 1, 0

    gcd, a1, b1 = extended_gcd(y, x % y)
    a = b1
    b = a1 - (x // y) * b1

    return gcd, a, b


res2 = 0
for i in range(0, len(lines), 4):
    A, B, P = process_input(i, True)
    # P cannot be spanned by vectors A and B
    if (A.y / A.x > P.y / P.x and B.y / B.x > P.y / P.x) or (
        A.y / A.x < P.y / P.x and B.y / B.x < P.y / P.x
    ):
        continue

    gcd, a, b = extended_gcd(A.x, B.x)
    # No combo of A and B can achieve an x value of P.x
    if P.x % gcd != 0:
        continue

    a *= P.x // gcd
    b *= P.x // gcd
    # the vector P - (aA + bB) has form <0, Y>
    Y = P.y - a * A.y - b * B.y
    lcm = math.lcm(A.x, B.x)
    # this is the smallest increment y can move by independently
    y = A.y * (lcm // A.x) - B.y * (lcm // B.x)
    if Y % y != 0:
        continue
    # (lcm/Ax)*A + (lcm/Bx)*B has form <0,y>
    a += (Y // y) * (lcm // A.x)
    b -= (Y // y) * (lcm // B.x)
    if a > 0 and b > 0:
        res2 += 3 * a + b

print(res2)
