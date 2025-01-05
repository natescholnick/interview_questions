# largest palindrome product of two 3-digit numbers

res = 0
for a in range(999, 99, -1):
    for b in range(a, 99, -1):
        if a * b < res:
            break
        if str(a * b) == str(a * b)[::-1]:
            res = max(res, a * b)

print(res)
