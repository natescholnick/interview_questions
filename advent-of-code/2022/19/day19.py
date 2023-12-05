import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/19/example.txt') as f:
    lines = f.read().splitlines()

for line in lines[:1]:
    geodes_produced = 0
    ore_robot_ore_cost, clay_robot_ore_cost, ob_robot_ore_cost, ob_robot_clay_cost, geo_robot_ore_cost, geo_robot_ob_cost = [
        int(c) for c in line.split(' ')]


def dfs(resources, robots, time):
    if time == 24:
        return resources[3]
    res = 0


# Given some iteration of dfs, we need to calculate our options, which is itself a linear combinations problem
# Specifically, given resource values A, B, and C
# Find all linear combinations of (a1), (a2), (a3, b3), and (a4, c4) such that their sum is less than or equal to (A, B, C)

def getOptions(resources, robots):
    options = [[0, 0, 0, 0]]    # build nothing
    if resources[2] >= geo_robot_ob_cost and resources[0] >= geo_robot_ore_cost:  # build geode robot
        options.append([0, 0, 0, 1])
    if resources[1] >= ob_robot_clay_cost and resources[0] >= ob_robot_ore_cost:
        next_resources = [resources[0] - ob_robot_ore_cost,
                          resources[1] - ob_robot_clay_cost, resources[2], resources[3]]
        next_robots = robots[:]
        next_robots[2] += 1
        options.append((next_resources, next_robots))
    if resources[0] >= clay_robot_ore_cost:
        next_resources = [resources[0] - clay_robot_ore_cost,
                          resources[1], resources[2], resources[3]]
        next_robots = robots[:]
        next_robots[1] += 1
        options.append((next_resources, next_robots))
    if resources[0] >= ore_robot_ore_cost:
        next_resources = [resources[0] - ore_robot_ore_cost,
                          resources[1], resources[2], resources[3]]
        next_robots = robots[:]
        next_robots[0] += 1
        options.append((next_resources, next_robots))
    return options

# def getOptions(resources, robots):
#     options = []
#     if resources[2] >= geo_robot_ob_cost and resources[0] >= geo_robot_ore_cost:
#         next_resources = [resources[0] - geo_robot_ore_cost,
#                           resources[1], resources[2] - geo_robot_ob_cost, resources[3]]
#         next_robots = robots[:]
#         next_robots[3] += 1
#         options.append((next_resources, next_robots))
#     if resources[1] >= ob_robot_clay_cost and resources[0] >= ob_robot_ore_cost:
#         next_resources = [resources[0] - ob_robot_ore_cost,
#                           resources[1] - ob_robot_clay_cost, resources[2], resources[3]]
#         next_robots = robots[:]
#         next_robots[2] += 1
#         options.append((next_resources, next_robots))
#     if resources[0] >= clay_robot_ore_cost:
#         next_resources = [resources[0] - clay_robot_ore_cost,
#                           resources[1], resources[2], resources[3]]
#         next_robots = robots[:]
#         next_robots[1] += 1
#         options.append((next_resources, next_robots))
#     if resources[0] >= ore_robot_ore_cost:
#         next_resources = [resources[0] - ore_robot_ore_cost,
#                           resources[1], resources[2], resources[3]]
#         next_robots = robots[:]
#         next_robots[0] += 1
#         options.append((next_resources, next_robots))
#     options.append(([resources[i] + robots[i] for i in range(4)], robots))
#     return options


print(getOptions([12, 10, 7, 0], [3, 2, 1, 0]))
