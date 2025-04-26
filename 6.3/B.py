# Реклама на билбордах


def Merge(n1: list, n2: list) -> list:
    n = []
    i, j = 0, 0
    while len(n1) > i and len(n2) > j:
        if n1[i][0] > n2[j][0]:
            n.append(n1[i])
            i += 1
        else:
            n.append(n2[j])
            j += 1
    return n + n1[i:] + n2[j:]


def MergeSort(n: list) -> list:
    if len(n) <= 1:
        return n
    
    n1, n2 = n[:len(n) // 2], n[len(n) // 2:]
    n1, n2 = MergeSort(n1), MergeSort(n2)
    return Merge(n1, n2)


def main():
    n, k, w = map(int, input().split())  # билбордов, рекламодателей, недель
    places, max_profit = n * w, 0        # доступно мест, максимальная прибыль
    offers = []                          # [платит за неделю, максимум недель]
    for _ in range(k):
        offers.append(list(map(int, input().split())))
        
    for offer in offers:
        best_busy = min(places, offer[1])   # сколько места займёт
        places -= best_busy                 # занимаем место
        max_profit += offer[0] * best_busy  # фиксируем прибыль
        if places == 0:                     # закончилось место: стоп
            break
    
    print(max_profit)


if __name__ == "__main__":
    main()
