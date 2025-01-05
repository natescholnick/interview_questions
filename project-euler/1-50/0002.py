# sum of even Fibonacci numbers below 4 million

fib = [1, 1]
res = 0
while fib[-1] < 4000000:
    fib.append(fib[-1] + fib[-2])
    if fib[-1] % 2 == 0:
        res += fib[-1]
print(res)
