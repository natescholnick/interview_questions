import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/24/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
wire_names = set()
wires = {}
# el = (wire1, wire2, type, out wire, gate id)
gates = defaultdict(list)

is_wire = True
for line in lines:
    if len(line) == 0:
        is_wire = False
        continue
    if is_wire:
        wire, val = line.split(": ")
        wires[wire] = int(val)
        wire_names.add(wire)
    else:
        gate, out = line.split(" -> ")
        a, op, b = gate.split(" ")
        gates[a].append((a, b, op, out, tuple(sorted([a, b, out]))))
        gates[b].append((b, a, op, out, tuple(sorted([a, b, out]))))
        wire_names.update({a, b, out})

res = 0
q = deque([])
needs = defaultdict(list)
seen = set()
for wire in wires:
    matched = set()
    for gate in needs[wire]:
        q.append(gate)
        matched.add(gate[-1])
    needs[wire] = []
    for gate in gates[wire]:
        if gate[-1] not in matched:
            complement = gate[1]
            needs[complement].append(gate)


compute_gate = {
    "AND": lambda a, b: wires[a] & wires[b],
    "OR": lambda a, b: wires[a] | wires[b],
    "XOR": lambda a, b: wires[a] ^ wires[b],
}

while q:
    # look at a gate with both input wires already computed
    a, b, op, out, id = q.popleft()

    # no repeats
    if id in seen:
        continue
    seen.add(id)

    # save the output wire's value
    wires[out] = compute_gate[op](a, b)

    # add all gates missing this output to the queue
    matched = set()
    for gate in needs[out]:
        q.append(gate)
        matched.add(gate[-1])
    needs[out] = []

    # indicate which gates are half complete
    for gate in gates[out]:
        if gate[-1] not in matched:
            complement = gate[1]
            needs[complement].append(gate)

# True, so far so good
# print(sorted(list(wire_names)) == sorted(wires.keys()))

res = 0
bits = sorted(filter(lambda x: x[0] == "z", wires.keys()), reverse=True)
for bit in bits:
    res *= 2
    res += wires[bit]

print(res)

# Part 2
#
res2 = 0
