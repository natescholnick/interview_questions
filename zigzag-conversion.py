# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

def convert(s, numRows):
    solution = ''
    interval = 2 * (numRows - 1)
    if numRows == 1:
        return s
    for row in range(numRows):
        if row == 0:
            substring = ''.join([s[x]
                                 for x in range(len(s)) if x % interval == 0])
        elif row == numRows - 1:
            substring = ''.join([s[x] for x in range(
                len(s)) if x % interval == interval // 2])
        else:
            substring = ''.join([s[x] for x in range(
                len(s)) if x % interval == row or x % interval == interval - row])
        solution += substring

    return solution


print(convert('PAYPALISHIRING', 3))
