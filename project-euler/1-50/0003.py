# largest prime factor of 600851475143

num = 600851475143
for factor in range(2, int(600851475143 ** (1 / 2))):
    while num % factor == 0:
        num //= factor
    if num == 1:
        print(factor)
        break
