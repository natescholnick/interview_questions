from collections import deque
from math import lcm
import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/11/input.txt') as f:
    lines = f.read().splitlines()


monkeys = []
mod = 1


class Monkey:
    def __init__(self, items, inspect_param, test_param, passes_to):
        self.items = deque([])
        for item in items:
            self.items.append(item)
        self.inspect_param = inspect_param
        self.test_param = test_param
        self.passes_to = passes_to
        self.passes = 0

    def inspect(self, x):
        op, val = self.inspect_param
        if op == '+':
            return x + int(val)
        else:
            if val == 'old':
                return x**2
            else:
                return int(val) * x

    def test(self, x): return x % int(self.test_param) == 0

    def receive(self, item):
        self.items.append(item)

    def run_items(self):
        while self.items:
            self.passes += 1
            item = self.items.popleft()
            # '// 3' instead of '% mod' for Part 1
            item = self.inspect(item) % mod
            monkeys[self.passes_to[self.test(item)]].receive(item)


for i in range(0, len(lines), 6):
    items = [int(x) for x in lines[i].split(' ')]
    passes_to = [int(lines[i+4]), int(lines[i+3])]
    monkeys.append(Monkey(items, lines[i+1].split(' '), lines[i+2], passes_to))
    mod = lcm(int(lines[i+2]), mod)


for _ in range(10000):  # Part 1 range(20)
    for monkey in monkeys:
        monkey.run_items()

active = sorted(monkeys, key=lambda x: x.passes)
print(active[-1].passes * active[-2].passes)
