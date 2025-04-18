# Сортировка выбором


def SelectionSort(n: int, data: list) -> None:
    for i in range(n):
        min_element = min(data[i:])
        min_element_index = data[i:].index(min_element) + i
        data[i], data[min_element_index] = min_element, data[i]


def main():
    n = int(input())
    data = list(map(int, input().split()))
    SelectionSort(n, data)
    print(*data)
    
    
if __name__ == "__main__":
    main()
