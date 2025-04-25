# Наибольший общий делитель


def GCD(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return max(a, b)
    return GCD(b, a % b)


def main():
    a, b = map(int, input().split())
    print(GCD(a, b))


if __name__ == "__main__":
    main()
