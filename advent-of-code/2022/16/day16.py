from collections import defaultdict
import functools
import os

# cwd = os.getcwd()

# with open(f'{cwd}/advent-of-code/2022/16/input.txt') as f:
#     lines = f.read().splitlines()

# flows = {}
# G = {}

# for line in lines:
#     line = line.split(' ')
#     flows[line[0]] = int(line[1])
#     G[line[0]] = line[2:]

# cur = 'AA'


# @functools.lru_cache(maxsize=None)
# def dfs(valve, opened, time):
#     if time <= 0:
#         return 0
#     res = 0
#     if valve not in opened:
#         pressure = flows[valve] * (time - 1)
#         open_valve = tuple(sorted(opened + (valve,)))
#         for nei in G[valve]:
#             res = max(res, pressure +
#                       dfs(nei, open_valve, time - 2))
#             res = max(res, dfs(nei, opened, time - 1))
#     return res


# print(dfs('AA', (), 30))

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/16/input.txt') as f:
    lines = f.read().splitlines()

graph = {}
flows = {}
for line in lines:
    line = line.split(' ')
    x = line[0]
    flows[x] = int(line[1])
    graph[line[0]] = line[2:]

nodeId = defaultdict(lambda: len(nodeId))
# only assign consecutive ids to non-zero flows
[nodeId[u] for u in flows if flows[u]]
ALL_MASK = (1 << len(nodeId)) - 1

cache = defaultdict(
    lambda: [[-1 for mask in range(ALL_MASK + 1)] for t in range(31)])


def dp(u, t, mask):
    if t == 0:
        return 0
    if cache[u][t][mask] == -1:
        best = max(dp(v, t - 1, mask) for v in graph[u])
        bit = 1 << nodeId[u]
        if bit & mask:
            best = max(best, dp(u, t - 1, mask - bit) + flows[u] * (t - 1))
        cache[u][t][mask] = best
    return cache[u][t][mask]


print("Part1", dp("AA", 30, ALL_MASK))
print("Part2", max(dp("AA", 26, ALL_MASK - mask) + dp("AA", 26, mask)
                   for mask in range(ALL_MASK + 1)))
