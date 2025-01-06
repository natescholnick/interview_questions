# Pythagorean triple (a, b, c) such that a + b + c = 1000

for a in range(1, 330):
    for b in range(a + 1, 500):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            res = a * b * c
            print(f"Pythagorean triple: {a}, {b}, {c}")
            break
print(res)
