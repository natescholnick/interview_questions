# sum of primes below 2 million
res = 2
for i in range(3, 2000000, 2):
    is_prime = True
    for j in range(3, int(i**0.5) + 1, 2):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        res += i

print(res)
