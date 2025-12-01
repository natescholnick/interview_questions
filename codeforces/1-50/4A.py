def solve(w: int):
    print(["NO", "YES"][w > 3 and w % 2 == 0])


def main():
    w = int(input())
    solve(w)


if __name__ == "__main__":
    main()
