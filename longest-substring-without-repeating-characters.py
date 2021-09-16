# Given a string s, find the length of the longest substring without repeating characters.

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

def lengthOfLongestSubstring(s):
    substring = ''
    solution = 0

    for i in range(len(s)):
        if s[i] in substring:
            substring = substring[substring.index(s[i]) + 1:] + s[i]
            continue

        substring += s[i]

        if len(substring) > solution:
            solution = len(substring)

    return solution


print(lengthOfLongestSubstring('abadc'))
