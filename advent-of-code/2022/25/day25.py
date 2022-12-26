import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/25/input.txt') as f:
    lines = f.read().splitlines()

# get decimal sum
total = 0
for line in lines:
    cur = 0
    for c in line:
        cur = 5 * cur + int(c.replace('-', '-1').replace('=', '-2'))
    total += cur

# convert to base 5
digits = []
while total:
    digits.append(total % 5)
    total //= 5

# convert to SNAFU
carry = 0
res = ''
for digit in digits:
    num = int(digit) + carry
    if num in {0, 1, 2}:
        carry = 0
        res += str(num)
        continue
    carry = 1
    res += ['=', '-', '0'][num - 3]

print(res[::-1])

# It won't let me do part 2 until I've finished all the other problems RIP
