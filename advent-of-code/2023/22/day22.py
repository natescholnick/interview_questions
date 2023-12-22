import os
from collections import defaultdict, deque, Counter
import re
import heapq
import math

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/22/input.txt") as f:
    lines = f.read().splitlines()


# Part 1
# Observe that the first coordinate is always less than the second
# and that the longest sand bricks are 5 units long
l = 0
maxs = [0] * 3
for line in lines:
    x1, y1, z1, x2, y2, z2 = [int(x) for x in line.split(' ')]
    maxs[0] = max(maxs[0], x1, x2)
    maxs[1] = max(maxs[1], y1, y2)
    maxs[2] = max(maxs[2], z1, z2)
    l = max(l, x2-x1, y2-y1, z2-z1)

# print(maxs) # 9, 9, 315
# print(l) # 4 (segments are all short)
    
G = [[[-1] * (maxs[2] + 1) for _ in range(maxs[1] + 1)] for __ in range(maxs[1] + 1)]
m = len(lines)

def createBlock(i: int, q: heapq) -> None:
    x1, y1, z1, x2, y2, z2 = [int(x) for x in lines[i].split(' ')]
    diffs = [(x2-x1), (y2-y1), (z2-z1)]
    l = max(diffs) + 1
    inc = [int(bool(x)) for x in diffs]

    # priority queue based upon distance from the ground
    heapq.heappush(q, (z1, x1, y1, l, inc, i))

    # write blocks into 3 space
    for _ in range(l):
        G[x1][y1][z1] = i
        x1 += inc[0]
        y1 += inc[1]
        z1 += inc[2]


def canLower(block: list[list[int]]) -> bool:
    return all([z > 1 and G[x][y][z-1] == -1 for x, y, z in block])


def lowerBlock(qItem: tuple) -> None:
    z1, x1, y1, l, inc, id = qItem
    block = [[x1 + c * inc[0], y1 + c * inc[1], z1 + c * inc[2]] for c in range(l)]
    # unwrite block
    for x, y, z in block:
        G[x][y][z] = -1
    # lower block
    while canLower(block):
        for i in range(l):
            block[i][2] -= 1
    # write block into new position and check collisions
    else:
        for x, y, z in block:
            G[x][y][z] = id
            if G[x][y][z-1] not in {-1, id}:
                above[G[x][y][z-1]].add(id)
                below[id].add(G[x][y][z-1])

# q elements are of the form:
# coordinates (z first for falling prio), block length, block orientation vector, block id
q = []
for i in range(m):
    createBlock(i, q)

above, below = defaultdict(set), defaultdict(set)
while q:
    lowerBlock(heapq.heappop(q))

res = 0
for i in range(m):
    adjs = above[i]
    if len(adjs) == 0:
        res += 1
        continue
    soloSupport = False
    for adj in adjs:
        if len(below[adj]) == 1:
            soloSupport = True
            break
    res += not soloSupport

print(res)

# Part 2
cache = {}
def countFalling(blockId: int) -> set[int]:
    if len(above[blockId]) == 0:
        return {blockId}
    falling = set()
    cascade = deque([])
    cascade.append(blockId)
    while cascade:
        id = cascade.popleft()
        falling.add(id)
        supported = above[id]
        for block in supported:
            if below[block].issubset(falling):
                cascade.append(block)
    return falling

res2 = 0
for blockId in range(m):
    if blockId not in cache:
        cache[blockId] = countFalling(blockId)
    res2 += len(cache[blockId]) - 1

print(res2)
