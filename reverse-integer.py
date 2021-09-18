# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# -231 <= x <= 231 - 1

def reverse(x):
    sign = 1
    if x < 0:
        sign = -1
        x *= -1
    sol = sign*int(str(x)[::-1])
    if (abs(sol) > (2 ** 31 - 1)):
        return 0
    return sol


print(reverse(-123))
