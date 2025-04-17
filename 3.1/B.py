# Сочетания
# P.S. Пока шёл со станции МЦК "Стрешнево" в МАИ, догадался до нужного условия


def P(n: int) -> int:
    if n == 0:
        return 1
    return n * P(n - 1)


def C(numbers: list[int, int]) -> int:
    n, k = numbers[0], numbers[1]
    if n == k:
        return 1
    if n < k:
        return 0
    return P(n) // (P(n - k) * P(k))

       
print(C(list(map(int, input().split()))))
