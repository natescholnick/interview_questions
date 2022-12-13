from functools import cmp_to_key
import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/13/input.txt') as f:
    lines = f.read().splitlines()

n = len(lines)


def compare(x, y):  # True if x is "less than" y
    ordered = None
    if isinstance(x, int) and isinstance(y, int):
        if x != y:
            return x < y
        return None
    if isinstance(x, list) and isinstance(y, list):
        i = -1
        for i in range(len(x)):
            if i >= len(y):
                return False
            ordered = compare(x[i], y[i])
            if ordered != None:
                break
        if ordered == None and i < len(y) - 1:
            return True
    else:
        if type(x) == int:
            ordered = compare([x], y)
        else:
            ordered = compare(x, [y])
    return ordered


# Part 1
res = 0
for i in range(0, n, 3):
    left, right = eval(lines[i]), eval(lines[i+1])
    if compare(left, right):
        res += i//3 + 1
print(res)

# Part 2
arr = [[[2]], [[6]]]
for line in lines:
    if len(line) > 1:
        arr.append(eval(line))

# The native comparison function thinks of x > y as truthy, but
# the problem statement led me to define compare(x, y) such that x < y → True
# Hence setting reverse to True
arr.sort(reverse=True, key=cmp_to_key(lambda x, y: compare(x, y) - 0.5))

a, b = arr.index([[2]]), arr.index([[6]])
print((a + 1) * (b + 1))
