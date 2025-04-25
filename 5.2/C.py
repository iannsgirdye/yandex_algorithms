# Наибольшее число шагов алгоритма Евклида


def F(n: int) -> int:
    last, current = 0, 1
    
    while current + last <= n:
        now = current + last
        current, last = now, current
    
    return last, current


def main():
    n = int(input())
    print(*F(n))


if __name__ == "__main__":
    main()
