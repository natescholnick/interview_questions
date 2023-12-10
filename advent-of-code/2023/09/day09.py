import os
from collections import defaultdict

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/09/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
def findNext(seq):
    subseqs = [seq]
    while not all(x == 0 for x in subseqs[-1]):
        next_subseq = []
        for i in range(1, len(subseqs[-1])):
            next_subseq.append(subseqs[-1][i] - subseqs[-1][i-1])
        subseqs.append(next_subseq)
    
    return sum([x[-1] for x in subseqs])

res = 0
for line in lines:
    res += findNext([int(x) for x in line.split(' ')])
print(res)

# Part 2
def findPrev(seq):
    subseqs = [seq]
    while not all(x == 0 for x in subseqs[-1]):
        next_subseq = []
        for i in range(1, len(subseqs[-1])):
            next_subseq.append(subseqs[-1][i] - subseqs[-1][i-1])
        subseqs.append(next_subseq)
    
    return sum([subseqs[i][0] * (-1 if i%2 else 1) for i in range(len(subseqs))])

res2 = 0
for line in lines:
    res2 += findPrev([int(x) for x in line.split(' ')])
print(res2)