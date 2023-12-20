import os
from collections import defaultdict, deque, Counter
import re
import heapq
import math

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/20/input.txt") as f:
    lines = f.read().splitlines()


# Part 1
class Module:
    def __init__(self, name, destinations=None):
        self.name = name
        if destinations == None:
            destinations = []
        self.out = destinations
    
class FF(Module):
    def __init__(self, name, destinations=None, on=False):
        super().__init__(name, destinations)
        self.on = on

    def receive(self, pulse, _):
        if pulse == 1:
            return []
        self.on = not self.on
        return [(adj, 1 if self.on else 0, self.name) for adj in self.out]

class Conj(Module):
    def __init__(self, name, destinations=None, inputs=None):
        super().__init__(name, destinations)
        if inputs == None:
            inputs = {}
        self.inc = inputs
    
    def addInput(self, input):
        self.inc[input] = 0
    
    def receive(self, pulse, sender):
        self.inc[sender] = pulse
        if all(v for v in self.inc.values()):
            return [(adj, 0, self.name) for adj in self.out]
        return [(adj, 1, self.name) for adj in self.out]

class Broadcast(Module):
    def __init__(self, name, destinations=None):
        super().__init__(name, destinations)
    
    def receive(self, pulse, _):
        return [(adj, pulse, self.name) for adj in self.out]

conjs = set()
lookup = {}
for line in lines:
    mod, outs = line.split(' ')[0], line.split(' ')[1:]
    if mod == 'broadcaster':
        lookup[mod] = Broadcast(mod, outs)
    type, name = mod[0], mod[1:]
    if type == '%':
        lookup[name] = FF(name, outs)
    if type == '&':
        lookup[name] = Conj(name, outs)
        conjs.add(name)

for line in lines:
    name, outs = line.split(' ')[0], line.split(' ')[1:]
    name = name.lstrip('%&')
    for out in outs:
        if out in conjs:
            lookup[out].addInput(name)

# module network built
# pulse syntax: (destination, pulse type, sender)
            
low, high = 0, 0
def pushButton():
    global low, high
    q = deque([])
    q.append(('broadcaster', 0, 'button'))
    p1, p2, p3, p4 = [], [], [], []
    while q:
        name, pulse, sender = q.popleft()
        
        # part 1 code
        # if pulse:
        #     high += 1
        # else:
        #     low += 1

        # part 2 code
        if name == 'rd':
            p1.append(pulse)
        if name == 'bt':
            p2.append(pulse)
        if name == 'fv':
            p3.append(pulse)
        if name == 'pr':
            p4.append(pulse)

        if name not in lookup:
            continue

        for nextPulse in lookup[name].receive(pulse, sender):
            q.append(nextPulse)
    return (p1, p2, p3, p4)

# part 1 solution
# for _ in range(1000):
#     pushButton()
# print(low * high)

# Part 2
# Brute force is probably too slow, so let's LCM some cycles:
# Low to rx mean vd needs high from rd, bt, fv, pr
# So we look for low pulses sent to RD, BT, FV, and PR

rd, bt, fv, pr = [], [], [], []
for _ in range(20000):
    signals = pushButton()
    rd.append(signals[0])
    bt.append(signals[1])
    fv.append(signals[2])
    pr.append(signals[3])

def printPattern(mod):
    for i in range(len(mod)):
        if 0 in mod[i]:
            print(i, mod[i])
    print('\n')

printPattern(rd)
printPattern(bt)
printPattern(fv)
printPattern(pr)

# recurrences are at 3911, 3917, 3929, and 3793 respectively
print(math.lcm(3911, 3917, 3929, 3793))


