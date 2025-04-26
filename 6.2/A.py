# Специи


def main():
    n, W = map(int, input().split())  # кол-во специй и вместимость рюкзака
    spices = []                       # специи вида [цена за единицу, вес]
    result = 0                        # стоимость унесённых специй
    for _ in range(n):
        price, weight = map(int, input().split())
        value = price / weight
        spices.append([value, weight])
    
    while W > 0 and max(spices, key=lambda x: x[0]) != [0, 0]:
        max_index = spices.index(max(spices, key=lambda x: x[0]))  # индекс самого ценного оставшегося
        max_weight = min(W, spices[max_index][1])                  # сколько можно забрать
        W -= max_weight                                            # забрали
        result += spices[max_index][0] * max_weight                # пополнили банк стоимостью
        spices[max_index][0], spices[max_index][1] = 0, 0          # обнулили, чтобы отметить, что закончился

    print(result)


if __name__ == "__main__":
    main()
