import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np
import time


cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/22/input.txt") as f:
    lines = f.read().splitlines()


# Part 1
# modulo is 2^24
def next_secret(num):
    num = num ^ (num << 6) % 16777216
    num = num ^ (num >> 5) % 16777216
    num = num ^ (num << 11) % 16777216
    return num


start = time.time()

res = 0
for line in lines:
    num = int(line)
    for _ in range(2000):
        num = next_secret(num)
    res += num

end = time.time()

print(f"\nPart 1 completed in: {end - start} seconds.")
print(f"Result: {res}\n")

# Part 2
all_insignia = set()


def generate_change_insignia(num):
    changes = []
    out = defaultdict(int)
    p = num % 10
    for _ in range(2000):
        new_num = next_secret(num)
        changes.append(new_num % 10 - p)
        num = new_num
        p = new_num % 10
        if len(changes) >= 4 and tuple(changes[-4:]) not in out:
            all_insignia.add(tuple(changes[-4:]))
            out[tuple(changes[-4:])] = p
    return out


start = time.time()

price_per_change = []  # len 2000, el = {(last 4 changes): price}
for line in lines:
    price_per_change.append(generate_change_insignia(int(line)))

all_insignia = list(all_insignia)

end = time.time()

print(f"Secret insignia generated in: {end - start} seconds.")
print(f"Total change insignia found: {len(all_insignia)}")

start = time.time()

res2 = 0
for key in all_insignia:
    bananas = 0
    for secret in price_per_change:
        bananas += secret[key]
    res2 = max(res2, bananas)

end = time.time()

print(f"\nPart 2 price computation completed in: {end - start} seconds.")
print(f"Result: {res2}\n")

# Over 40 seconds altogether, oof
