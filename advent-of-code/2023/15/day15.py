import os
from collections import defaultdict, deque, Counter
import re

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/15/input.txt") as f:
    l = f.read()

# Part 1
def hashValue(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256
    return val


steps = l.split(',')
res = 0
for step in steps:
    res += hashValue(step)
print(res)

# Part 2
boxes = [[] for _ in range(256)]

for step in steps:
    lens = None
    if '-' in step:
        label = step[:-1]
        box = hashValue(label)
        boxes[box] = [x for x in boxes[box] if x[0] != label]
    else:
        label, lens = step.split('=')
        box = hashValue(label)
        replaced = False
        for i in range(len(boxes[box])):
            if boxes[box][i][0] == label:
                boxes[box][i][1] = lens
                replaced = True
                break
        if not replaced:
            boxes[box].append([label, lens])

res2 = 0
for box in range(256):
    for slot in range(len(boxes[box])):
        res2 += (box + 1) * (slot + 1) * int(boxes[box][slot][1])
print(res2)

            
