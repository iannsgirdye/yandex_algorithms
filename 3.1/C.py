# Сочетания с повторениями


def P(n: int) -> int:
    if n == 0:
        return 1
    return n * P(n - 1)


def A(n: int, k: int) -> int:
    return P(k + n - 1) // (P(k) * P(n - 1))


def main():
    n, k = map(int, input().split())
    print(A(n, k))


if __name__ == "__main__":
    main()
