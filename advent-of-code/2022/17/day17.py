import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/17/input.txt') as f:
    lines = f.read()

# Part 1
n = len(lines)
jet_id = 0
tower = [['_'] * 7]
height = 0

rocks = {0: [(0, 0), (0, 1), (0, 2), (0, 3)],
         1: [(0, 0), (0, 1), (1, 1), (-1, 1), (0, 2)],
         2: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
         3: [(0, 0), (1, 0), (2, 0), (3, 0)],
         4: [(0, 0), (0, 1), (1, 0), (1, 1)]}


def push(rock, i, j):
    go = lines[jet_id % n]
    if rock == 0:
        if go == '<' and j > 0 and (i >= len(tower) or tower[i][j-1] == '.'):
            return -1
        if go == '>' and j < 3 and (i >= len(tower) or tower[i][j+4] == '.'):
            return 1

    elif rock == 1:
        if go == '<' and j > 0 and (i-1 >= len(tower) or tower[i-1][j] == '.') and (i >= len(tower) or tower[i][j-1] == '.') and (i+1 >= len(tower) or tower[i+1][j] == '.'):
            return -1
        if go == '>' and j < 4 and (i-1 >= len(tower) or tower[i-1][j+2] == '.') and (i >= len(tower) or tower[i][j+3] == '.') and (i+1 >= len(tower) or tower[i+1][j+2] == '.'):
            return 1

    elif rock == 2:
        if go == '<' and j > 0 and (i >= len(tower) or tower[i][j-1] == '.') and (i+1 >= len(tower) or tower[i+1][j+1] == '.') and (i+2 >= len(tower) or tower[i+2][j+1] == '.'):
            return -1
        if go == '>' and j < 4 and (i >= len(tower) or tower[i][j+3] == '.') and (i+1 >= len(tower) or tower[i+1][j+3] == '.') and (i+2 >= len(tower) or tower[i+2][j+3] == '.'):
            return 1

    elif rock == 3:
        if go == '<' and j > 0 and all([(i+k >= len(tower) or tower[i+k][j-1] == '.') for k in range(4)]):
            return -1
        if go == '>' and j < 6 and all([(i+k >= len(tower) or tower[i+k][j+1] == '.') for k in range(4)]):
            return 1

    else:
        if go == '<' and j > 0 and all([(i+k >= len(tower) or tower[i+k][j-1] == '.') for k in range(2)]):
            return -1
        if go == '>' and j < 5 and all([(i+k >= len(tower) or tower[i+k][j+2] == '.') for k in range(2)]):
            return 1

    return 0


def fall(rock, i, j):
    if rock == 0:
        return i-1 >= len(tower) or all([tower[i-1][j+k] == '.' for k in range(4)])
    elif rock == 1:
        return all([i-1 >= len(tower) or tower[i-1][j] == tower[i-1][j+2] == '.', i-2 >= len(tower) or tower[i-2][j+1] == '.'])
    elif rock == 2:
        return i-1 >= len(tower) or all([tower[i-1][j+k] == '.' for k in range(3)])
    elif rock == 3:
        return i-1 >= len(tower) or tower[i-1][j] == '.'
    else:
        return i-1 >= len(tower) or all([tower[i-1][j+k] == '.' for k in range(2)])


def writeToTower(rock, i, j):
    added_height = {0: 0, 1: 1, 2: 2, 3: 3, 4: 1}
    while len(tower) < i + added_height[rock] + 1:
        tower.append(['.'] * 7)
    for x, y in rocks[rock]:
        tower[i+x][j+y] = '#'
    return added_height[rock] + i


def drop_rock(rock):
    global jet_id
    global height
    i, j = height + 4, 2
    if rock == 1:
        i += 1
    moving = True
    while moving:
        j += push(rock, i, j)
        jet_id += 1
        if fall(rock, i, j):
            i -= 1
        else:
            moving = False
    height = max(height, writeToTower(rock, i, j))


loop = 1740
for rock in range(2022):
    drop_rock(rock % 5)

print(f'Part 1: {height}')


# Part 2
# The work is done, the simulation is built. 1 trillion is far too many rocks to simulate
# The problem here is to find the modular patterns and do the arithmetic

# len(input) = 10091 (mod basis for pattern looping)
# rock looping pattern: num_loops * 1740 - 6, always repeating with jet_id = 2
# loops needed: 574712643, remainder: 1180 (add 6)
# height on loop: 2749 5508 8267 11026 13785
#                      2759 2759 2759
# HEIGHT = 2759 * loops - 10, 1585632182027
# Remainder of 1186 adds 7388 - 5508 = 1888
print(f'Part 2: {1888 + 1585632182027}')
