# Given a string s, return the longest palindromic substring in s.

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

def longestPalindrome(s):
    substringOdd = ''
    substringEven = ''
    skipOdd = False
    skipEven = False
    solution = ''
    x = 1
    for i in range(len(s)):
        substringOdd = s[i]
        if len(s) > 1 and i != len(s) - 1:
            if s[i] == s[i+1]:
                substringEven = s[i:i+2]
            else:
                skipEven = True
        while i - x >= 0 and i + x < len(s):
            if s[i-x] == s[i+x] and not skipOdd:
                substringOdd = s[i+x] + substringOdd + s[i+x]
            else:
                skipOdd = True
            if i + x + 1 == len(s):
                break
            if s[i-x] == s[i+x+1] and not skipEven:
                substringEven = s[i-x] + substringEven + s[i-x]
            else:
                skipEven = True
            if skipOdd and skipEven:
                break
            x += 1

        print(i, substringOdd)
        if len(substringOdd) > len(solution):
            solution = substringOdd
        if len(substringEven) > len(solution):
            solution = substringEven
        substringOdd = ''
        substringEven = ''
        skipOdd = False
        skipEven = False
        x = 1
    return solution


print(longestPalindrome('caba'))
