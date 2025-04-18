# Сортировка слиянием


def Merge(lst1: list, lst2: list) -> list:
    new_lst = []
    len_lst1, len_lst2 = len(lst1), len(lst2)
    i, j = 0, 0
    while i < len_lst1 and j < len_lst2:
        if lst1[i] < lst2[j]:
            new_lst.append(lst1[i])
            i += 1
        else:
            new_lst.append(lst2[j])
            j += 1

    new_lst += lst1[i:] + lst2[j:]
    return new_lst


def MergeSort(lst: list) -> list:
    if len(lst) == 1:
        return lst
    half = len(lst) // 2
    lst1, lst2 = lst[:half], lst[half:]
    sorted_lst1, sorted_lst2 = MergeSort(lst1), MergeSort(lst2)
    sorted_lst = Merge(sorted_lst1, sorted_lst2)
    return sorted_lst
    

def main():
    input()
    lst = list(map(int, input().split()))
    print(*MergeSort(lst))
    
    
if __name__ == "__main__":
    main()
