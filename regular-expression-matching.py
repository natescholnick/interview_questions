# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# 1 <= s.length <= 20
# 1 <= p.length <= 30
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

def isMatch(s, p):
    dp_table = [[False] * (len(s) + 1) for false in range(len(p) + 1)]
    dp_table[0][0] = True

    for i in range(1, len(p) + 1):
        dp_table[i][0] = i > 1 and dp_table[i-2][0] and p[i-1] == '*'

    for i in range(1, len(p) + 1):
        for j in range(1, len(s) + 1):
            if p[i-1] == s[j-1] or p[i-1] == '.':
                dp_table[i][j] = dp_table[i][j] or dp_table[i-1][j-1]

            elif p[i-1] == '*':
                dp_table[i][j] = dp_table[i][j] or dp_table[i-1][j]
                dp_table[i][j] = dp_table[i][j] or (i > 1 and dp_table[i-2][j])

                if i > 1 and p[i-2] in {s[j-1],  '.'}:
                    dp_table[i][j] = dp_table[i][j] or dp_table[i][j-1]

    return dp_table[-1][-1]


print(isMatch("aaa", "ab*a*c*a"))
