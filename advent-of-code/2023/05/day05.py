import os
import bisect

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/05/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
locations = []
lineStarts = []
for i in range(1, len(lines)):
    if len(lines[i]) > 0 and lines[i][0].isalpha():
        lineStarts.append(i + 1)


def incrementMapValue(lineStart, key):
    for line in lines[lineStart:]:
        if len(line) == 0:
            return key
        destination, source, length = [int(x) for x in line.split(" ")]
        if key >= source and key < source + length:
            return destination + key - source
    return key


for seed in [int(x) for x in lines[0].split(" ")]:
    loc = seed
    for start in lineStarts:
        loc = incrementMapValue(start, loc)
    locations.append(loc)

print(min(locations))

# Part 2
seeds = [int(x) for x in lines[0].split(" ")]
intervals = []
for i in range(0, len(seeds), 2):
    intervals.append((seeds[i], seeds[i] + seeds[i + 1] - 1))


def generateMap(lineStart):
    startToDest = {}
    ordering = []
    for line in lines[lineStart:]:
        if len(line) == 0:
            return sorted(ordering), startToDest
        destination, start, length = [int(x) for x in line.split(" ")]
        ordering.extend([start, start + length - 1])
        startToDest[start] = destination - start
    ordering.sort()

    return ordering, startToDest


# We have some set of intervals of seeds
# Pass the intervals through a mapping by splitting and recombining them
# Proceed through each map until a final set of intervals is reached
for startLineOfMapping in lineStarts:
    mapIntervals, mappingToNextInterval = generateMap(startLineOfMapping)
    newIntervals = []
    while intervals:
        start, end = intervals.pop()
        insertionPoint = bisect.bisect_right(mapIntervals, start)
        # Start of seed interval does have a corresponding map or
        # handle edge case: our seed interval start has one seed of overlap with a mapping end
        # (but gets inserted at an even index because we're using bisect RIGHT)
        if insertionPoint % 2 or (
            insertionPoint > 0 and start == mapIntervals[insertionPoint - 1]
        ):
            if not insertionPoint % 2:
                insertionPoint -= 1
            transformValue = mappingToNextInterval[mapIntervals[insertionPoint - 1]]
            newStart = start + transformValue
            # Our seed range fits entirely within a single mapping line
            if mapIntervals[insertionPoint] >= end:
                newIntervals.append((newStart, end + transformValue))
            # Split this seed interval, sending the first section through the map
            # and the second section back into the old intervals we're currently looping through
            else:
                newIntervals.append(
                    (newStart, mapIntervals[insertionPoint] + transformValue)
                )
                intervals.append((mapIntervals[insertionPoint] + 1, end))
        # Start of seed interval is not specified in the map (beware endpoint indices)
        else:
            # Our seed range fits entirely in the gap between mappings (fully mapped to self)
            if (
                insertionPoint == len(mapIntervals)
                or end < mapIntervals[insertionPoint]
            ):
                newIntervals.append((start, end))
            # Split the seed interval, but without the use of our mapping function
            else:
                newIntervals.append((start, mapIntervals[insertionPoint] - 1))
                intervals.append((mapIntervals[insertionPoint], end))
    intervals = newIntervals

print(min([x for x, _ in intervals]))
