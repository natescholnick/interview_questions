import os
from collections import Counter

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/07/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
royals = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
groups = {50: [], 40: [], 32: [], 30: [], 22: [], 20: [], 10: []}
for line in lines:
    hand, bid = line.split(" ")
    bid = int(bid)
    type = sorted(list(Counter(hand).values()))
    if type == [5]:
        groups[50].append((hand, bid))
    elif type == [1, 4]:
        groups[40].append((hand, bid))
    elif type == [2, 3]:
        groups[32].append((hand, bid))
    elif type == [1, 1, 3]:
        groups[30].append((hand, bid))
    elif type == [1, 2, 2]:
        groups[22].append((hand, bid))
    elif type == [1, 1, 1, 2]:
        groups[20].append((hand, bid))
    else:
        groups[10].append((hand, bid))


def val(card):
    if card in royals:
        return royals[card]
    return int(card)


rank = 1
res = 0
for group in sorted(groups.keys()):
    groups[group].sort(
        key=lambda x: (
            val(x[0][0]),
            val(x[0][1]),
            val(x[0][2]),
            val(x[0][3]),
            val(x[0][4]),
        )
    )
    for _, bid in groups[group]:
        res += rank * bid
        rank += 1

print(res)

# Part 2
royals["J"] = 1
groups = {50: [], 40: [], 32: [], 30: [], 22: [], 20: [], 10: []}
for line in lines:
    hand, bid = line.split(" ")
    bid = int(bid)
    cardCount = Counter(hand)
    jokers = cardCount["J"]

    if jokers == 5:
        cardCount = {"J": 0}
    else:
        del cardCount["J"]

    weightedHand = sorted(list(cardCount.values()))
    weightedHand[-1] += jokers
    if weightedHand == [5]:
        groups[50].append((hand, bid))
    elif weightedHand == [1, 4]:
        groups[40].append((hand, bid))
    elif weightedHand == [2, 3]:
        groups[32].append((hand, bid))
    elif weightedHand == [1, 1, 3]:
        groups[30].append((hand, bid))
    elif weightedHand == [1, 2, 2]:
        groups[22].append((hand, bid))
    elif weightedHand == [1, 1, 1, 2]:
        groups[20].append((hand, bid))
    else:
        groups[10].append((hand, bid))


def val(card):
    if card in royals:
        return royals[card]
    return int(card)


rank = 1
res = 0
for group in sorted(groups.keys()):
    groups[group].sort(
        key=lambda x: (
            val(x[0][0]),
            val(x[0][1]),
            val(x[0][2]),
            val(x[0][3]),
            val(x[0][4]),
        )
    )
    for _, bid in groups[group]:
        res += rank * bid
        rank += 1

print(res)
