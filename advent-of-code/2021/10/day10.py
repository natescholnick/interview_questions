import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2021/10/input.txt') as f:
    lines = f.read().splitlines()


closers = {')': '(', ']': '[', '}': '{', '>': '<'}

# Part 1
corruption_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
res = 0
for line in lines:
    stack = []
    for c in line:
        if c in closers:
            if not stack or stack.pop() != closers[c]:
                res += corruption_scores[c]
        else:
            stack.append(c)
print(res)

# Part 2
incomplete_scores = {'(': 1, '[': 2, '{': 3, '<': 4}
scores = []
for line in lines:
    score = 0
    stack = []
    corrupt = False
    for c in line:
        if c in closers:
            if not stack or stack.pop() != closers[c]:
                corrupt = True
                break
        else:
            stack.append(c)
    if corrupt:
        continue
    for c in stack[::-1]:
        score = 5 * score + incomplete_scores[c]
    scores.append(score)

print(sorted(scores)[len(scores)//2])
