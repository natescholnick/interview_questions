# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

# Constraints:
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].

def decodeString(self, s: str) -> str:
    # FIRST PASS, Time limit exceeded. Optimization below
    # res, i, stack = '', 0, []
    # while i < len(s):
    #     if s[i] == ']':
    #         # decrement k and either pop or repeat top of stack
    #         stack[-1][0] -= 1
    #         if stack[-1][0] == 0:
    #             stack.pop()
    #             i += 1
    #         else:
    #             i = stack[-1][1]
    #     elif s[i].isdigit():
    #         stack.append([int(s[i]), i+2])
    #         i += 2
    #     else: #letter
    #         res += s[i]
    #         i += 1
    # return res
    
    res, i, stack = '', 0, []
    while i < len(s):
        if s[i] == ']':
            k, prev_str = stack.pop()
            k_chunk = res[prev_str:]
            res += (k-1) * k_chunk
            i += 1
        elif s[i].isdigit():
            j = i
            while s[j].isdigit():
                j += 1
            stack.append([int(s[i:j]), len(res)])
            i = j+1
        else:
            res += s[i]
            i += 1
    return res