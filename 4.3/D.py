# Максимальное произведение четырех чисел


from random import randint


MIN_N = 3
MAX_N = 2 * 10 ** 5
MIN_A = -2 * 10 ** 4
MAX_A = 2 * 10 ** 4


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
    return max(
        a[0] * a[1] * a[2] * a[3],
        a[0] * a[1] * a[-1] * a[-2],
        a[-1] * a[-2] * a[-3] * a[-4]
    )
    

def SlowMultiply(n: int, a: list) -> int:
    result = -2 * MIN_A ** 4
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    current_result = a[i] * a[j] * a[k] * a[l]
                    if current_result > result:
                        result = current_result
    return result


def test():
    while True:
        n = randint(MIN_N, MAX_N)
        a = [randint(MIN_A, MAX_A) for _ in range(n)]
        
        result1 = FastMultiply(a)
        result2 = SlowMultiply(n, a)
        if result1 == result2:
            print("OK")
        else:
            print(n, a, result1, result2)
            break
    
    
def main():
    _ = input()
    a = list(map(int, input().split()))
    print(FastMultiply(a))
    
    
if __name__ == "__main__":
    main()
