# Сувениры


def main():
    n, s = map(int, input().split())
    MAX = s + 1
    count = 0
    prices = []
    for _ in range(n):
        prices.append(int(input()))
    
    while s - min(prices) >= 0 and min(prices) != MAX:
        min_index = prices.index(min(prices))  # индекс самого дешёвого товара
        s -= prices[min_index]                 # купили
        prices[min_index] = MAX                # больше нет на прилавке
        count += 1
    
    print(count)


if __name__ == "__main__":
    main()
