# 10001st prime number
import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


primes = []
num = 2
while len(primes) < 10001:
    if is_prime(num):
        primes.append(num)
    num += 1

print(primes[-1])
