# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'. ([]){}

def isValid(s):
    openers = {'(', '{', '['}
    matches = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    unmatched_openers = []
    for char in s:
        if char in openers:
            unmatched_openers.append(char)
        else:
            if not unmatched_openers:
                return False
            if unmatched_openers[-1] == matches[char]:
                del unmatched_openers[-1]
            else:
                return False

    return not bool(unmatched_openers)


print(isValid(''))


# list = [1, 2, 3, 1]
# dict = {'a': 'apple',
#      'b': 'bear',
#      'c': 'clam'}
# set = {1, 2, 3}

# print(s[1])
