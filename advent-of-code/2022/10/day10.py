import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/10/input.txt') as f:
    lines = f.read().splitlines()

# Part 1
res = 0
cycles = [1, 1, 1]
x = 1
for line in lines:
    line = line.split(' ')
    if len(line) == 1:
        cycles.append(x)
    else:
        x += int(line[1])
        cycles.append(x)
        cycles.append(x)

for i in range(20, 221, 40):
    res += i * cycles[i]

print(res)

# Part 2
for i in range(1, 241, 40):
    row = ''
    for j in range(0, 40):
        if (cycles[i+j] % 40 - j) % 40 < 2 or (j - cycles[i+j] % 40) % 40 < 2:
            row += '#'
        else:
            row += '.'
    print(row)

#  Output:
#  ####.###...##..###..#....####.####.#..#.
#  ...#.#..#.#..#.#..#.#....#.......#.#..#.
#  ..#..#..#.#..#.#..#.#....###....#..#..#.
#  .#...###..####.###..#....#.....#...#..#.
#  #....#.#..#..#.#.#..#....#....#....#..#.
#  ####.#..#.#..#.#..#.####.#....####..##.. ~ ZRARLFZU
