import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2022/19/input.txt") as f:
    lines = f.read().splitlines()


# Part 1
# first approach did dfs by minute, but that was far too slow
# as an optimization, let's instead do dfs by next bot to build
class Blueprint:
    def __init__(self, costs, duration=24):
        self.duration = duration
        self.costs = costs
        self.inv = {"ore": 0, "clay": 0, "obs": 0, "geo": 0}
        self.bots = {"ore": 1, "clay": 0, "obs": 0, "geo": 0}
        self.time = 1
        self.max_ore_needs = max(
            costs["ore"]["ore"],
            costs["clay"]["ore"],
            costs["obs"]["ore"],
            costs["geo"]["ore"],
        )
        self.max_geodes = -1

    def gather(self):
        return [self.bots["ore"], self.bots["clay"], self.bots["obs"], self.bots["geo"]]

    def pocket(self, resouces, t):
        self.inv["ore"] += resouces[0] * t
        self.inv["clay"] += resouces[1] * t
        self.inv["obs"] += resouces[2] * t
        self.inv["geo"] += resouces[3] * t
        self.time += t

    def unpocket(self, resouces, t):
        self.inv["ore"] -= resouces[0] * t
        self.inv["clay"] -= resouces[1] * t
        self.inv["obs"] -= resouces[2] * t
        self.inv["geo"] -= resouces[3] * t
        self.time -= t

    def time_needed(self, bot):
        time = 0
        for resource, cost in self.costs[bot].items():
            if self.inv[resource] < cost:
                time = max(
                    time, math.ceil((cost - self.inv[resource]) / self.bots[resource])
                )
        # +1 to account for the time it takes to build the bot
        return time + 1

    def build_choices(self):
        choices = []
        if (
            self.bots["obs"] > 0
            and (t := self.time_needed("geo")) <= self.duration - self.time
        ):
            choices.append(("geo", t))
        if (
            self.bots["clay"] > 0
            and self.bots["obs"] < self.costs["geo"]["obs"]
            and (t := self.time_needed("obs")) <= self.duration - self.time
        ):
            choices.append(("obs", t))
        if (
            self.bots["clay"] < self.costs["obs"]["clay"]
            and (t := self.time_needed("clay")) <= self.duration - self.time
        ):
            choices.append(("clay", t))
        if (
            self.bots["ore"] < self.max_ore_needs
            and (t := self.time_needed("ore")) <= self.duration - self.time
        ):
            choices.append(("ore", t))
        return choices

    def build(self, bot):
        self.bots[bot] += 1
        for resource, cost in self.costs[bot].items():
            self.inv[resource] -= cost

    def unbuild(self, bot):
        self.bots[bot] -= 1
        for resource, cost in self.costs[bot].items():
            self.inv[resource] += cost

    def dfs(self):
        # End state
        if self.time == self.duration:
            self.max_geodes = max(self.max_geodes, self.inv["geo"] + self.bots["geo"])
            return
        # If it's no longer possible to achieve a new max, abort
        if (
            (self.duration - self.time) * (self.duration + 1 - self.time)
        ) // 2 + self.inv["geo"] + (self.duration + 1 - self.time) * self.bots[
            "geo"
        ] <= self.max_geodes:
            return

        # check what we can build (based upon resouces gathered up to this point, but not during this minute)
        choices = self.build_choices()
        # now gather resources, remember what we gather in order to backtrack
        resources = self.gather()
        # build something
        for choice, time in choices:
            self.pocket(resources, time)
            self.build(choice)
            self.dfs()
            self.unbuild(choice)
            self.unpocket(resources, time)
        # if we can't build anything, gather resources until the end
        if not choices:
            time_left = self.duration - self.time
            self.pocket(resources, time_left)
            self.dfs()
            self.unpocket(resources, time_left)


blueprints = []
for line in lines:
    words = line.strip().split(" ")
    costs = {
        "ore": {"ore": int(words[6])},
        "clay": {"ore": int(words[12])},
        "obs": {"ore": int(words[18]), "clay": int(words[21])},
        "geo": {"ore": int(words[27]), "obs": int(words[30])},
    }
    blueprints.append(Blueprint(costs))

res = 0
for i in range(len(blueprints)):
    blueprints[i].dfs()
    print(f"Blueprint {i + 1} complete. Max geodes: {blueprints[i].max_geodes}")
    res += (i + 1) * blueprints[i].max_geodes

print(res)
