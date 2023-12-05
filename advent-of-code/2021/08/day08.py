import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2021/08/input.txt') as f:
    lines = f.read().splitlines()

# Part 1
res = 0
for line in lines:
    output = line.split(' | ')[1].split(' ')
    for value in output:
        if len(value) in {2, 3, 4, 7}:
            res += 1
print(res)

# Part 2
res2 = 0
for line in lines:
    uniques = {2: 1, 3: 7, 4: 4, 7: 8}
    to_nums = {}
    to_code = {}

    input, output = line.split(' | ')
    input, output = input.split(' '), output.split(' ')

    for code in input:
        if len(code) in uniques:
            to_nums[code] = uniques[len(code)]
            to_code[uniques[len(code)]] = code
    # 5: 2, 3, 5
    for code in input:
        if len(code) == 5:
            if sum([c in code for c in to_code[4]]) == 2:
                to_nums[code] = 2
                to_code[2] = code
            elif all([c in code for c in to_code[1]]):
                to_nums[code] = 3
                to_code[3] = code
            else:
                to_nums[code] = 5
                to_code[5] = code
    # 6: 0, 6, 9
    for code in input:
        if len(code) == 6:
            if sum([c in code for c in to_code[5]]) == 4:
                to_nums[code] = 0
                to_code[0] = code
            elif not all([c in code for c in to_code[1]]):
                to_nums[code] = 6
                to_code[6] = code
            else:
                to_nums[code] = 9
                to_code[9] = code
    # collect output terms
    for code in input:
        for perm in output:
            if set(perm) == set(code):
                to_nums[perm] = to_nums[code]

    value = 0
    for code in output:
        value = 10 * value + to_nums[code]
    res2 += value

print(res2)
