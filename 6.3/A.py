# Рекламная кампания


def QuickSort(n: list) -> list:
    if len(n) <= 1:
        return n
    
    m = len(n) // 2
    n_small, n_large = [], []
    for i in range(len(n)):
        if i != m:
            if n[i] > n[m]:
                n_small.append(n[i])
            else:
                n_large.append(n[i])
    
    n_small = QuickSort(n_small)
    n_large = QuickSort(n_large)
    
    return n_small + [n[m]] + n_large


def main():
    n = int(input())
    prices = QuickSort(list(map(int, input().split())))
    clicks = QuickSort(list(map(int, input().split())))
    
    result = 0
    for i in range(n):
        result += prices[i] * clicks[i]
    
    print(result)


if __name__ == "__main__":
    main()
