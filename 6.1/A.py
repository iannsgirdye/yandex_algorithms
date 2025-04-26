# Размен: все варианты


def main():
    money = int(input())
    count = 0
    coins = [money, money // 5, money // 10]
    results = []
    
    for coin10 in range(coins[2] + 1):
        for coin5 in range(coins[1] - (2 * coin10) + 1):
            for coin1 in range(coins[0] - (10 * coin10 + 5 * coin5) + 1):
                if coin1 + coin5 * 5 + coin10 * 10 == money:
                    count += 1
                    results.append((coin1, coin5, coin10))
    
    print(count)
    for coins_ in results:
        result = str(sum(coins_)) + " " + "1 " * coins_[0] + "5 " * coins_[1] + "10 " * coins_[2]
        print(result.rstrip())


if __name__ == "__main__":
    main()
