# Покрытие точек отрезками одинаковой длины


def QuickSort(data: list) -> list:
    if len(data) <= 1:
        return data
    
    m = len(data) // 2
    small, large = [], []
    for i in range(len(data)):
        if i != m:
            if data[i] < data[m]:
                small.append(data[i])
            else:
                large.append(data[i])
    
    small, large = QuickSort(small), QuickSort(large)
    return small + [data[m]] + large


def main():
    n, L = map(int, input().split())
    data = QuickSort(list(map(int, input().split())))

    count, right = 1, data[0] + L    
    for i in range(n):
        if data[i] > right:
            right = data[i] + L
            count += 1

    print(count)


if __name__ == "__main__":
    main()
