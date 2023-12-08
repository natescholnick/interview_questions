import os
from collections import defaultdict

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/08/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

directions = lines[0]
n = len(directions)

# build graph
node_lookup = {}
for line in lines[2:]:
    val, l, r = line.split(' ')
    node = Node(val=val, left=l, right=r)
    node_lookup[val] = node

steps = 0
curr = node_lookup['AAA']
while curr.val != 'ZZZ':
    if directions[steps % n] == 'L':
        curr = node_lookup[curr.left]
    else:
        curr = node_lookup[curr.right]
    steps += 1
print(steps)

# Part 2
steps = 0

# Firstly we can do away with node_lookup and gather the starting points
curr_nodes = []
loopStarts = []
loopLengths = []
for node in node_lookup.values():
    if node.val.endswith('A'):
        curr_nodes.append(node)
    node.left = node_lookup[node.left]
    node.right = node_lookup[node.right]

def takeStep(node, step):
    if directions[step] == 'L':
        return node.left
    return node.right

for i in range(len(curr_nodes)):
    curr = curr_nodes[i]
    seen = {curr: 0}
    loops = 0
    loopFound = False
    while not loopFound:
        for step in range(n):
            curr = takeStep(curr, step)
        loops += 1
        if curr in seen:
            loopFound = True
        else:
            seen[curr] = loops

    loopLengths.append(n * (loops - seen[curr]))

    # with a loop found, we count back n steps to find its exact starting point
    countback_starts = []
    for node, loop in seen.items():
        if loop == loops - 1 or loop == seen[curr] - 1:
            countback_starts.append(node)

    start, end = countback_starts

    for step in range(n):
        start = takeStep(start, step)
        end = takeStep(end, step)
        if start == end:
            loopStarts.append(n * (seen[curr] - 1) + step + 1)
            break

# Now knowing all paths lead-in and loop lengths, eliminate the lead-in
loopStart = max(loopStarts)
end_nodes = []
for i in range(len(curr_nodes)):
    curr_ends = []
    curr = curr_nodes[i]
    for step in range(loopStart + loopLengths[i]):
        if curr.val.endswith('Z'):
            curr_ends.append(step)
        curr = takeStep(curr, step % n)
    end_nodes.append(curr_ends)

# This problem seems to have been intentionally designed such that each loop
# only contains a single node ending in 'Z', a kind convenience leading to standard lcm
# The more general case of a lcm amongst sets of candidates would be challenging to solve
# and certainly curious to puzzle about in the head

# flatten
for i in range(len(end_nodes)):
    end_nodes[i] = end_nodes[i][0]

# get primes
primes = []
for num in range(2, max(end_nodes)):
    prime = True
    for divisor in primes:
        if num % divisor == 0:
            prime = False
            break
    if prime:
        primes.append(num)

# get prime factorizations
pfs = []
for _val in end_nodes:
    val = _val
    pf = defaultdict(int)
    for prime in primes:
        while val % prime == 0:
            pf[prime] += 1
            val //= prime
        if val == 1:
            break
    pfs.append(pf)

# determine lcm
lcm = defaultdict(int)
for factors in pfs:
    for factor, power in factors.items():
        lcm[factor] = max(lcm[factor], power)

res = 1
for factor, power in lcm.items():
    for _ in range(power):
        res *= factor

print(res)
