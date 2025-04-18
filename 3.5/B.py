# Слияние сортированных последовательностей


def Merge(lists: list[list]) -> None:
    new_list = []
    while len(lists) > 0:
        min_list = min(lists, key=lambda x: x[0])  # наименьший элемент среди всех последовательностей
        min_list_index = lists.index(min_list)     # индекс последовательности с наименьшим элементом
        new_list.append(min_list[0])
        if len(min_list) > 1:
            del lists[min_list_index][0]  # удаление наименьшего элемента из его последовательности
        else:
            del lists[min_list_index]     # удаление всей последовательности, если в ней был только наименьший элемент
    return new_list


def main():
    n = int(input())  # количество отсортированных последовательностей
    lists = []        # последовательности
    for _ in range(n):
        input()                                        # количество элементов последовательности
        lists.append(list(map(int, input().split())))  # элементы последовательности
    print(*Merge(lists))


if __name__ == "__main__":
    main()
