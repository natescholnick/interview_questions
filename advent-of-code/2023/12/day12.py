import os
from collections import defaultdict, deque, Counter
import re

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/12/input.txt") as f:
    lines = f.read().splitlines()


# Part 1
cache = {}


def dfs(seq, groups):
    res = 0
    minLen = sum(groups) + len(groups) - 1
    n, r = groups[0], groups[1:]
    for i in range(len(seq) - minLen + 1):
        if (
            any([c == "." for c in seq[i : i + n]])
            or i + n < len(seq)
            and seq[i + n] == "#"
        ):
            continue
        if not r:
            return 1
        else:
            if (seq[i + n + 1 :].lstrip("."), tuple(r)) not in cache:
                cache[(seq[i + n + 1 :].lstrip("."), tuple(r))] = dfs(
                    seq[i + n + 1 :].lstrip("."), r
                )
            res += cache[(seq[i + n + 1 :].lstrip("."), tuple(r))]
    return res


counts = 0
for line in lines:
    record = re.sub(r"\.+", ".", line.split(" ")[0].strip("."))
    groups = [int(x) for x in line.split(" ")[1].split(",")]
    if (record, tuple(groups)) not in cache:
        cache[(record, tuple(groups))] = dfs(record, groups)
    counts += cache[(record, tuple(groups))]

print(counts)
