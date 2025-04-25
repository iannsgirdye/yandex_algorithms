# Последняя цифра частичной суммы чисел Фибоначчи
"""РЕШЕНИЕ НЕ ПРОШЛО ВСЕ ТЕСТЫ"""


def F(m: int, n: int) -> int:
    """
    if m % 60 == 0:
        i > m + 1  =>  before -- const
        S_n = F(n + 2) - 1  =>  current - before = current - 1
    else:
        S = F(n + 2) - F(m + 1)  =>  (current - 1) - (before - 1) = current - before
    """
    before = 1 if m % 60 == 0 else 0
    m, n = (m + 1) % 60, (n + 2) % 60
    last, current = 0, 1
    
    for i in range(2, n + 1):
        now = (current + last) % 10
        current, last = now, current
        if i == m:
            before = current
    
    # 7 - 4 = 3;  4 - 7 = -3,  14 - 7 = 7  =>  -3 % 10 = 7
    return (current - before) % 10


def main():
    m, n = map(int, input().split())
    print(F(m, n))


if __name__ == "__main__":
    main()
