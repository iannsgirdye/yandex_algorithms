# Максимальное произведение


from random import random


def algorithm_1(n: int, numbers: list) -> int:
    index1 = 0
    for i in range(n):
        if numbers[i] > numbers[index1]:
            index1 = i
    
    index2 = 0 if index1 != 0 else 1
    for i in range(n):
        if numbers[i] > numbers[index2] and i != index1:
            index2 = i

    return numbers[index1] * numbers[index2]


def algorithm_2(n: int, numbers: list) -> int:
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            current_result = numbers[i] * numbers[j]
            if current_result > result:
                result = current_result
    return result


def test():
    while True:
        n = int(random() * 1000) + 2
        numbers = [int(random() * 1000) for _ in range(n)]
        result1 = algorithm_1(n, numbers)
        result2 = algorithm_2(n, numbers)
        if result1 != result2:
            print(n, numbers, result1, result2)
            break


def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    print(algorithm_1(n, numbers))
    
    
if __name__ == "__main__":
    main()
