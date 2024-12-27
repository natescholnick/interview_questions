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
# el = (wire1, wire2, operation, out wire) Note: out wire also serves as a gate id
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
        gates[a].append((a, b, op, out))
        gates[b].append((b, a, op, out))
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
    a, b, op, out = q.popleft()

    # no repeats
    if out in seen:
        continue
    seen.add(out)

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
# Alright, fix the binary adder... a few things:
# it takes 7 gates to optimally go from Xn and Yn to Zn:
# 2 gates to calculate the value: Xn XOR Yn XOR Cn-1, where C is a carry bit
# 5 gates to compute the carry bit: (Xn AND Yn) OR (Xn and Cn-1) OR (Yn and Cn-1)
# the least significant bit is the exception, 2 gates:
# z0 = x0 XOR y0, c0 = x0 AND y0
# so optimal N-bit addition uses 7N - 5 gates
# In this case we're looking at 45 bit addition, which means
# 310 gates (or more, a potential added dimension of trickery)

# Secondly, any output bit Zn should only be influenced by bits Xm and Ym, where m <= n

# So, a good place to start will be checking for superfluous gates
# and running dfs from z bits back to x and y bits to find any invalid paths
# that must contain output swap(s)

# Additionally, we should be able to fix the adder bit by bit
# that is, if addition is working for numbers 31 and down,
# then all gates involed in processing x0-x5, y0-y5 are free of swaps


def gate_id(a, b, op):
    return tuple(sorted([a, b]) + [op])


is_gate = False
gates_by_output = {}
gates_by_input = {}
for line in lines:
    if len(line) == 0:
        is_gate = True
        continue
    if not is_gate:
        continue
    eq, out = line.split(" -> ")
    a, op, b = eq.split(" ")
    gates_by_output[out] = gate_id(a, b, op)
    gates_by_input[gate_id(a, b, op)] = out

# print(len(gates_by_output))
# 222 gates... how is that possible? Carry on and hopefully learn on the way!
# Nah I just thought about it with paper and pen for a couple minutes:
# since we already have two XOR gates to determine the z bit, we reuse:
# Given the intermediary An = Xn XOR Yn,
# Cn = (An AND Cn-1) OR (Xn AND Yn), that is:
# Carry a 1 if: Exactly 1 input bit AND the previous carry bit OR both input bits are 1
# 7N - 5 becomes 5N - 3 and 5 * 45 - 3 = 222. nice :)

# From glancing at the input, it appears gates are always combined in the same way, eg
# z = ((x XOR y) XOR c)
# In reality, bits x, y, and c are indistinguishable in function, but I'll forego that hassle


def check_addition():
    pass


swaps = {
    "dbp": "fdv",
    "fdv": "dbp",
    "ckj": "z15",
    "z15": "ckj",
    "kdf": "z23",
    "z23": "kdf",
    "rpp": "z39",
    "z39": "rpp",
}
carry = "rfg"
# x, y, a = x XOR y, b = x AND y, c = a AND carry, new carry = b OR c
levels = [["x00", "y00", "rfg"]]
to_check = set()
# simple 0th case done manually
for i in range(1, 45):
    new_level = []
    bit = ""
    if i < 10:
        bit += "0"
    bit += str(i)

    x, y, z = "x" + bit, "y" + bit, "z" + bit
    z = swaps.get(z, z)
    new_level.extend([x, y])

    a = gates_by_input[gate_id(x, y, "XOR")]
    new_level.append(a)
    if a in swaps:
        a = swaps[a]
    else:
        to_check.add(a)

    # adding successfully up to this bit
    if gates_by_output[z] == gate_id(a, carry, "XOR"):
        to_check = set()
    # find the swap
    else:
        print(levels)
        print(to_check)
        break

    b = gates_by_input[gate_id(x, y, "AND")]
    new_level.append(b)
    if b in swaps:
        b = swaps[b]
    else:
        to_check.add(b)

    c = gates_by_input[gate_id(a, carry, "AND")]
    new_level.append(c)
    if c in swaps:
        c = swaps[c]
    else:
        to_check.add(c)

    carry = gates_by_input[gate_id(b, c, "OR")]
    new_level.append(carry)
    if carry in swaps:
        carry
    else:
        to_check.add(carry)
    carry = swaps.get(carry, carry)

    levels.append(new_level)

print(",".join(sorted(swaps.keys())))
