import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/15/input.txt') as f:
    lines = f.read().splitlines()


# Part 1
beacons_in_row = set()
restricted = set()
row = 2000000
for line in lines:
    x1, y1, x2, y2 = [int(a) for a in line.split(' ')]
    if y2 == row:
        beacons_in_row.add(y2)
    dist = abs(x1 - x2) + abs(y1 - y2) - abs(row - y1)
    if dist >= 0:
        for x in range(x1 - dist, x1 + dist + 1):
            restricted.add(x)

print(len(restricted) - len(beacons_in_row))


# This is what I originally did the night of
# I had to let my fan hum for about 30 seconds, but the correct answer was returned all the same
# The code is going through the rows one at a time, verifying that the intervals can be merged to cover [0, 4000000]

# # Part 2
# def mergeIntervals(arr):
#     arr.sort()
#     end = arr[0][1]
#     for i in range(1, len(arr)):
#         if arr[i][0] > end:
#             return end + 1
#         else:
#             end = max(end, arr[i][1])
#     return None


# M = [[int(a) for a in line.split(' ')] for line in lines]

# for row in range(4000001):
#     if row % 100000 == 0:
#         print(row)
#     intervals = []
#     for line in M:
#         x1, y1, x2, y2 = line
#         dist = abs(x1 - x2) + abs(y1 - y2) - abs(row - y1)
#         if dist >= 0:
#             intervals.append([x1 - dist, x1 + dist])
#     x = mergeIntervals(intervals)
#     if x != None:
#         coords = [x, row]
#         break

# print(coords)
# print(coords[0] * 4000000 + coords[1])


# Here's the refactored code for Part 2, which has a consistent runtime of <1 ms, approximately 100,000 time faster!
# The shell code is nearly the same, but instead of processing row by row, our helper function
# mergeIntervals makes decisions about which row is safe to skip ahead to

# Given two diamonds (rings in taxicab geometry), this function returns the greatest y-value at which they intersect
# Input rings have form [x, y, r] where (x, y) is the rings center and r is its radius
# It is called at a point when the following can be assured:
# On the given row, d1 has the leftmost left bound and d2 has the rightmost right bound. That is, they intersect.
# Figure out which edges intersect, then simply return the solution to that pair of linear equations


def intersectDiamonds(d1, d2):
    x1, y1, r1 = d1
    x2, y2, r2 = d2
    # In terms of the cases, imagine the unit ring |x| + |y| = 1
    # Label each side of this diamond 1 thru 4 based upon the quadrant it is in. That is:
    # 1: x + y = 1,     2: -x + y = 1       3: -x - y = 1       4: x - y = 1

    # Disclaimer! I had to draw this out to make sense of it.
    # If d2's side 2 is above d1's side 2 (comparing y-intercepts)
    if r1 + y1 - x1 < r2 + y2 - x2:    # 2, 3 case
        return (x2 - x1 + y1 + y2 + r1 - r2)//2
    # If d1's side 1 is above d2's side 1 (comparing y-intercepts)
    elif r1 + x1 + y1 > r2 + x2 + y2:  # 4, 1 case
        return (x2 - x1 + y1 + y2 + r2 - r1)//2
    # d1's side 1 intersecting d2's side 2 accounts for the remaining 4/6 cases
    else:                                           # 1, 2 case
        return (x1 - x2 + y1 + y2 + r1 + r2)//2


# Here we will compare the intervals as before, but in addition to the intervals we will also be passed the ring they come from
# This way, when two intervals do overlap, we can look back to the equations from which they came
# By calculating where the two rings intersect, we know their overlap is assured up to that point, and can move through the rows in massive chunks
# Our return value has the form [x value of answer (if found), next row where a current interval overlap will end]
def mergeIntervals(arr):
    last_overlap = 4000000
    arr.sort()
    prev = arr[0]
    for i in range(1, len(arr)):
        left_bound, right_bound, diamond = arr[i]
        # If the current interval is entirely contained within the previous, disregard it
        if right_bound <= prev[1]:
            continue
        # Since we're told there's a unique solution, the first gap must be it
        if left_bound > prev[1]:
            return [prev[1] + 1, None]
        # The intervals overlap. Our helper function will tell us the last row on which that remains true.
        else:
            last_overlap = min(
                last_overlap, intersectDiamonds(prev[2], diamond))
            prev = arr[i]

    return [None, last_overlap]


M = [[int(a) for a in line.split(' ')] for line in lines]

# Switched the for loop to a while loop so I could manually control which row to jump to
coords = [0, 0]
row = 0
while row <= 4000000:
    intervals = []
    for line in M:
        x1, y1, x2, y2 = line
        dist = abs(x1 - x2) + abs(y1 - y2) - abs(row - y1)
        if dist >= 0:
            intervals.append(
                [x1 - dist, x1 + dist, [x1, y1, abs(x1 - x2) + abs(y1 - y2)]])
    x, next_row = mergeIntervals(intervals)
    if x != None:
        coords = [x, row]
        break
    row = next_row + 1

print(coords)  # [3303271, 2906101]
print(coords[0] * 4000000 + coords[1])
