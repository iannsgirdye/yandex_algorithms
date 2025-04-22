# Максимальное произведение трех чисел


from random import randint


MIN_N = 3
MAX_N = 2 * 10 ** 5
MIN_A = -2 * 10 ** 5
MAX_A = 2 * 10 ** 5


def QuickSort(a: list) -> list:
    if len(a) <= 1:
        return a
    
    middle_index = len(a) // 2
    small_a = [a[i] for i in range(len(a)) if a[i] < a[middle_index]]
    large_a = [a[i] for i in range(len(a)) if a[i] >= a[middle_index] and i != middle_index]
    small_a = QuickSort(small_a)
    large_a = QuickSort(large_a)
    
    return small_a + [a[middle_index]] + large_a


def FastMultiply(a: list) -> int:
    a = QuickSort(a)
    return max(a[0] * a[1] * a[-1], a[-3] * a[-2] * a[-1])


def SlowMultiply(n: int, a: list) -> int:
    result = MIN_A - 1
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                current_result = a[i] * a[j] * a[k]
                if current_result > result:
                    result = current_result
    return result


def test():
    n = randint(MIN_N, MAX_N)
    a = [randint(MIN_A, MAX_A) for _ in range(n)]
    while True:
        result1 = FastMultiply(a)
        result2 = SlowMultiply(n, a)
        if result1 != result2:
            print(n, a, result1, result2)
            break
        else:
            print("OK")


def main():
    _ = input()
    a = list(map(int, input().split()))
    print(FastMultiply(a))


if __name__ == "__main__":
    main()
