import os
from collections import defaultdict, deque, Counter
import re

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/12/input.txt") as f:
    lines = f.read().splitlines()


# Part 1
cache = {}

def dfs(seq, groups):
    if seq == '':
        return 1 if groups == () else 0
    if groups == ():
        return 0 if '#' in seq else 1
    
    res = 0
    if seq[0] in '.?':
        if (seq[1:], groups) not in cache:
            cache[(seq[1:], groups)] = dfs(seq[1:], groups)
        res += cache[(seq[1:], groups)]
    if seq[0] in '#?':
        if groups[0] <= len(seq) and '.' not in seq[:groups[0]] and (groups[0] == len(seq) or seq[groups[0]] != '#'):
            if (seq[groups[0] + 1:], groups[1:]) not in cache:
                cache[(seq[groups[0] + 1:], groups[1:])] = dfs(seq[groups[0] + 1:], groups[1:])
            res += cache[(seq[groups[0] + 1:], groups[1:])]

    return res

counts = 0
for line in lines:
    record = re.sub(r"\.+", ".", line.split(" ")[0].strip("."))
    groups = tuple(map(int, line.split(" ")[1].split(",")))
    if (record, groups) not in cache:
        cache[(record, groups)] = dfs(record, groups)
    counts += cache[(record, groups)]

print(counts)

# Part 2
counts = 0
for line in lines:
    record = re.sub(r"\.+", ".", line.split(" ")[0])
    record = '?'.join([record] * 5)
    groups = tuple(map(int, line.split(" ")[1].split(","))) * 5
    if (record, groups) not in cache:
        cache[(record, groups)] = dfs(record, groups)
    counts += cache[(record, groups)]

print(counts)
