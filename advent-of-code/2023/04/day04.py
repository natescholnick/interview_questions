import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2023/04/input.txt') as f:
    lines = f.read().splitlines()

# Part 1
res = 0
for line in lines:
    winners, cards = line.split(' | ')
    winners = set(winners.split(' '))
    cards = cards.split(' ')
    matches = -1
    for card in cards:
        if card in winners:
            matches += 1
    if matches >= 0:
        res += 2**matches

print(res)

# Part 2
n = len(lines)
counts = [1 for _ in range(n)]

for i in range(n):
    winners, cards = lines[i].split(' | ')
    winners = set(winners.split(' '))
    cards = cards.split(' ')
    matches = 0
    for card in cards:
        if card in winners:
            matches += 1
            counts[i + matches] += counts[i]
print(sum(counts))
    
    