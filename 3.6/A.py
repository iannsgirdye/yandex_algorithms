# Разбиение Ломуто


def Lomuto(n: int, data: list) -> list:
    index_first_max, count_min = 0, 0
    for i in range(1, n):
        if data[i] > data[0] and index_first_max == 0:
            index_first_max = i
        elif data[i] < data[0]:
            count_min += 1
            if index_first_max > 0:
                data[i], data[index_first_max] = data[index_first_max], data[i]
                index_first_max += 1
    
    data[0], data[index_first_max - 1] = data[index_first_max - 1], data[0]
    return data


def main():
    n = int(input())
    data = list(map(int, input().split()))
    print(*Lomuto(n, data))


if __name__ == "__main__":
    main()
