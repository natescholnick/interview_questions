# LCM of 1 to 20
from collections import defaultdict


def prime_factors(n):
    factors = defaultdict(int)
    for i in range(2, n + 1):
        if i > n:
            break
        while n % i == 0:
            factors[i] += 1
            n //= i
    return factors


PF = defaultdict(int)
for num in range(2, 21):
    for factor, count in prime_factors(num).items():
        PF[factor] = max(PF[factor], count)

res = 1
for factor, count in PF.items():
    res *= factor**count

print(res)
