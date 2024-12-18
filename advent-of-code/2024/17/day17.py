import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2024/17/input.txt") as f:
    lines = f.read().splitlines()

registers = {}
for line in lines:
    if len(line) == 0:
        continue
    if line.startswith("Program"):
        program = [int(x) for x in line.split(": ")[1].split(",")]
    else:
        reg, val = line.split(": ")
        registers[reg[-1]] = int(val)

# Part 1
out = []


def combo(operand):
    if operand <= 3:
        return operand
    if operand == 4:
        return registers["A"]
    if operand == 5:
        return registers["B"]
    if operand == 6:
        return registers["C"]
    if operand == 7:
        print("Error: combo operand of 7 detected.")
        return


def execute(opcode, operand):
    if opcode == 0:
        registers["A"] = registers["A"] // (2 ** combo(operand))
    elif opcode == 1:
        registers["B"] = registers["B"] ^ operand
    elif opcode == 2:
        registers["B"] = combo(operand) % 8
    elif opcode == 3:
        if registers["A"]:
            return operand
    elif opcode == 4:
        registers["B"] = registers["B"] ^ registers["C"]
    elif opcode == 5:
        out.append(combo(operand) % 8)
    elif opcode == 6:
        registers["B"] = registers["A"] // (2 ** combo(operand))
    elif opcode == 7:
        registers["C"] = registers["A"] // (2 ** combo(operand))
    return


def part1():
    pointer = 0
    while pointer >= 0 and pointer < len(program):
        next = execute(program[pointer], program[pointer + 1])
        if next != None:
            pointer = next
        else:
            pointer += 2


part1()
print(",".join([str(x) for x in out]))

# Part 2

# Program (from the input) reads as follows:
# 2,4
# 1,2
# 7,5
# 4,3
# 0,3
# 1,7
# 5,5
# 3,0
# # answer is above 1000000, abondonning brute force
# for i in range(1000000):
#     registers["A"] = i
#     registers["B"] = 0
#     registers["C"] = 0
#     out = []
#     part1()
#     if out == program:
#         print(i)
#         break


# Writing down what the actual program does, I see we can work backwords:
def set_registers(A, B=0, C=0):
    global out
    registers["A"] = A
    registers["B"] = B
    registers["C"] = C
    out = []


# res2 = 0
# for digit in program[len(program) - 1 : 4 : -1]:
#     res2 <<= 3
#     for i in range(8):
#         set_registers(res2 + i)
#         part1()
#         if out[0] == digit:
#             res2 += i
#             break
# print(res2)
# print(oct(res2))
# set_registers(res2)
# part1()
# print(out)

# 46480617544, 0o532235370110_8 matches all but the first 4 digits
# but then the approach above fails...
# nearly there, I cannot ALWAYS take the lowest succcessful digit in the short term
# let's switch to dfs, since sometimes there are multiple options to match a digit


def dfs(A, power):
    if power == len(program):
        return A

    res = sys.maxsize
    digit = program[-power - 1]
    A <<= 3
    for i in range(8):
        set_registers(A + i)
        part1()
        if out[0] == digit:
            res = min(res, dfs(A + i, power + 1))

    return res


res2 = dfs(0, 0)
print(res2)
set_registers(res2)
part1()
print(out)
