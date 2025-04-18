# Быстрая сортировка


# правильнее назвать RandomizeQuickSort
def QuickSort(data: list) -> list:
    if len(data) <= 1:
        return data
    
    m = len(data) // 2
    c_small, c_large = [], []
    for i in range(len(data)):
        if i != m:
            if data[i] < data[m]:
                c_small.append(data[i])
            else:
                c_large.append(data[i])
            
    c_small = QuickSort(c_small)
    c_large = QuickSort(c_large)
    
    return c_small + [data[m]] + c_large
    
    
def main():
    input()
    data = list(map(int, input().split()))
    print(*QuickSort(data))
    
    
if __name__ == "__main__":
    main()
