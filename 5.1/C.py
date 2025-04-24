# Огромное число Фибоначчи


def pisanoPeriod(m: int) -> int:
    last, current = 0, 1
    period = 0
    while True:
        now = (current + last) % m
        current, last = now, current
        period += 1
        if last == 0 and current == 1:
            return period


def F(n: int, m: int) -> int:
    n %= pisanoPeriod(m)
    
    if n <= 1:
        return n
    
    last = 0
    current = 1
    for _ in range(2, n + 1):
        now = (current + last) % m
        current, last = now, current
    return current


def main():
    n, m = map(int, input().split())
    print(F(n, m))


if __name__ == "__main__":
    main()
