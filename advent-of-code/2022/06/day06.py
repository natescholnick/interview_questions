import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/6/input.txt') as f:
    lines = f.read().splitlines()


def findStartDepth(data, marker_length):
    res = marker_length
    marker = {}     # {k: v} of form {char: freq in previous marker_length charcters}

    for c in data[:marker_length]:
        marker[c] = marker.get(c, 0) + 1

    for i in range(marker_length, len(data)):
        if len(marker) == marker_length:
            break

        marker[data[i-marker_length]] -= 1
        if marker[data[i-marker_length]] == 0:
            del marker[data[i-marker_length]]

        marker[data[i]] = marker.get(data[i], 0) + 1
        res += 1

    return res


# Part 1
print(findStartDepth(lines[0], 4))

# Part 2
print(findStartDepth(lines[0], 14))
