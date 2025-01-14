import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2022/21/input.txt") as f:
    lines = f.read().splitlines()

m = len(lines)

# Part 1
arithmetic = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
}

screamed = {}
remaining = []
res = 0

for line in lines:
    name, data = line.split(": ")
    if " " not in data:
        screamed[name] = int(data)
    else:
        a, op, b = data.split(" ")
        remaining.append((name, a, b, op))

next_round = []
while len(screamed) < m:
    for name, a, b, op in remaining:
        if a in screamed and b in screamed:
            screamed[name] = arithmetic[op](screamed[a], screamed[b])
        else:
            next_round.append((name, a, b, op))
    remaining = next_round

print(screamed["root"])


# Part 2
# I realized this midday through part 1: it's cleaner to search backwards from "root"
# I also verified (code since removed) that each monkey's scream is only used as an operand once
# So no unexpected craziness when solving for "humn"
monkey_ops = {}
val = {}
for line in lines:
    name, data = line.split(": ")
    if " " in data:
        a, op, b = data.split(" ")
        monkey_ops[name] = (a, b, op)
    else:
        val[name] = int(data)


def find_humn(monkey):
    if monkey == "humn":
        return [monkey]
    if monkey in val:
        return None

    dep1, dep2, _ = monkey_ops[monkey]

    if l := find_humn(dep1):
        return l + [monkey]

    if r := find_humn(dep2):
        return r + [monkey]


def dfs(monkey):
    if monkey in val:
        return val[monkey]

    dep1, dep2, op = monkey_ops[monkey]

    return arithmetic[op](dfs(dep1), dfs(dep2))


path = find_humn("root")
path.pop()


def computable(x):
    if path[-1] != x:
        return x


def solve(a, b, op, eq):
    if op == "+":
        return eq - dfs(a if a else b)
    if op == "-":
        if a:
            return dfs(a) - eq
        else:
            return dfs(b) + eq
    if op == "*":
        return eq // dfs(a if a else b)
    if op == "/":
        if a:
            return dfs(a) // eq
        else:
            return eq * dfs(b)


# Begin with the solved side of the equation
a, b, _ = monkey_ops["root"]
RHS = dfs(a if path[-1] != a else b)

# Now at each loop, RHS is the value we need to make the next monkey along the path scream
while len(path) > 1:
    monkey = path.pop()
    a, b, op = monkey_ops[monkey]
    RHS = solve(computable(a), computable(b), op, RHS)

print(RHS)
