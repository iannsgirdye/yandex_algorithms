# Перестановки


def P(n: int) -> int:
    if n == 0:
        return 1
    return n * P(n - 1)


print(P(int(input())))
