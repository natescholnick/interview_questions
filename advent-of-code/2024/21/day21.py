import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/21/input.txt") as f:
    lines = f.read().splitlines()

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

# Part 1
numpad = {
    "A": (3, 2),
    "0": (3, 1),
    "X": (3, 0),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
}

arrowpad = {
    "A": (0, 2),
    "^": (0, 1),
    "X": (0, 0),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}


def gen_seq(code, pad=arrowpad):
    seq = []
    i0, j0 = pad["A"]
    for char in code:
        i1, j1 = pad[char]
        ix, jx = pad["X"]
        # must care to avoid the empty (X) space
        if ix in (i0, i1) and jx in (j0, j1):
            if i0 == ix:
                seq.extend(["^" if i1 < i0 else "v"] * abs(i0 - i1))
                seq.extend(["<" if j1 < j0 else ">"] * abs(j0 - j1))
            else:
                seq.extend(["<" if j1 < j0 else ">"] * abs(j0 - j1))
                seq.extend(["^" if i1 < i0 else "v"] * abs(i0 - i1))
        # Otherwise, try not to end on < since it's far from A on the arrowpad
        else:
            if j1 < j0:
                seq.extend(["<"] * (j0 - j1))
                seq.extend(["^" if i1 < i0 else "v"] * abs(i0 - i1))
            elif j1 == j0:
                seq.extend(["^" if i1 < i0 else "v"] * abs(i0 - i1))
            else:
                seq.extend(["^" if i1 < i0 else "v"] * abs(i0 - i1))
                seq.extend([">"] * (j1 - j0))
        seq.append("A")
        i0, j0 = i1, j1
    return "".join(seq)


def part1(num_bots=2):
    res = 0
    for code in lines:
        val = int(code[:-1])
        seq = gen_seq(code, numpad)
        for _ in range(num_bots):
            seq = gen_seq(seq)
        res += len(seq) * val

    print(res)


part1()

# Part 2
# runtime is a few seconds with 15 intermediary bots... optimizations needed for 25
# part1(15)
# optimization idea: group inputs by their return to the A button
# this makes them independent of order and context
# then count their generational offspring via a counter dictionary


def split_blocks(code):
    blocks = []
    next_block = ""
    for i in range(len(code)):
        next_block += code[i]
        if code[i] == "A":
            blocks.append(next_block)
            next_block = ""
    return blocks


# for arrowpad inputs referencing arrowpad inputs,
# there will be a small set of input blocks
blocks = set()
for but1 in arrowpad.keys():
    if but1 == "X":
        continue
    for but2 in arrowpad.keys():
        if but2 == "X":
            continue
        for block in split_blocks(gen_seq(but1 + but2)):
            blocks.add(block)

# {'vA', '>>A', '^A', '>^A', '<<A', '<^A', '<A', '>>^A', '>A', 'v<A', 'v>A', 'v<<A', '<vA', '^>A', 'A'}
# 15

# from code to numpad to first arrowpad, there are 24 arrowpads left.
# let's calculate 6th generation and then accumulate 4 times

gen_6 = defaultdict(lambda: {key: 0 for key in blocks})
for block in blocks:
    seq = block
    for _ in range(6):
        seq = gen_seq(seq)
    for chunk in split_blocks(seq):
        gen_6[block][chunk] += 1

gen_12 = defaultdict(lambda: {key: 0 for key in blocks})
for block in blocks:
    for chunk, coeff in gen_6[block].items():
        for desc, count in gen_6[chunk].items():
            gen_12[block][desc] += coeff * count

# print(sum([len(x) * y for x, y in gen_12["<A"].items()]))
# seq = "<A"
# for _ in range(12):
#     seq = gen_seq(seq)
# print(len(seq))
# It works!!

gen_24 = defaultdict(lambda: {key: 0 for key in blocks})
for block in blocks:
    for chunk, coeff in gen_12[block].items():
        for desc, count in gen_12[chunk].items():
            gen_24[block][desc] += coeff * count


res2 = 0
for code in lines:
    val = int(code[:-1])
    seq = gen_seq(gen_seq(code, numpad))
    for block in split_blocks(seq):
        res2 += val * sum([len(x) * y for x, y in gen_24[block].items()])

print(res2)
