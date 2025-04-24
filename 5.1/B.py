# Последняя цифра числа Фибоначчи


def F(n: int) -> int:
    if n <= 1:
        return n
    
    last, current = 0, 1
    for _ in range(2, n + 1):
        now = (current + last) % 10
        current, last = now, current
    return current


def main():
    n = int(input())
    print(F(n))


if __name__ == "__main__":
    main()
