def solve(args: list[int]):
    n, m, a = args
    print((n // a + (n % a > 0)) * (m // a + (m % a > 0)))


def main():
    args = [int(x) for x in input().split(" ")]
    solve(args)


if __name__ == "__main__":
    main()
