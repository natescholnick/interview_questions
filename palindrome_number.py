# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

# -2^31 <= x <= 2^31 - 1

def isPalindrome(x):
    x = str(x)
    for i in range(len(x)//2):
        if x[i] != x[-i-1]:
            return False

    return True


print(isPalindrome(12321))
