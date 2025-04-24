# Последняя цифра суммы чисел Фибоначчи


def F(n: int) -> int:
    if n <= 1:
        return n
    
    n = (n + 2) % 60
    if n == 0:
        return 9
    if n == 1:
        return 0
    
    last, current = 0, 1
    for _ in range(2, n + 1):
        now = (current + last) % 10
        current, last = now, current
    return current - 1 if current > 0 else 9


def main():
    n = int(input())
    print(F(n))


if __name__ == "__main__":
    main()
