# Сбор подписей


def Merge(data1: list, data2: list) -> list:
    data = []
    i, j = 0, 0
    
    while len(data1) > i and len(data2) > j:
        if data1[i][1] < data2[j][1]:
            data.append(data1[i])
            i += 1
        else:
            data.append(data2[j])
            j += 1
    
    return data + data1[i:] + data2[j:]


def MergeSort(data: list) -> list:
    if len(data) == 1:
        return data
    
    data1, data2 = data[:len(data) // 2], data[len(data) // 2:]
    data1, data2 = MergeSort(data1), MergeSort(data2)
    return Merge(data1, data2)


def main():
    n = int(input())           # всего сегментов
    segments, points = [], []  # сегменты и точки сбора
    for _ in range(n):
        segments.append(list(map(int, input().split())))
    segments = MergeSort(segments)
    
    for i in range(n):
        if segments[i] != None:            # если сегмент не обработан:
            points.append(segments[i][1])    # фиксируем точку сбора
            for j in range(i + 1, n):        # ищем сегменты, которые точка может покрыть:
                if segments[j] != None: 
                    if segments[j][0] <= segments[i][1]:  # сегмент начался до точки:
                        segments[j] = None                  # сегмент обработан
            segments[i] = None               # сегмент-инициатор также обработан
    
    print(len(points))
    print(*points)


if __name__ == "__main__":
    main()
