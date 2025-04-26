# Размен: 1, 5, 10, 20, 50


def main():
    money = int(input())
    coins = (
        money // 50,
        (money % 50) // 20,
        ((money % 50) % 20) // 10,
        (((money % 50) % 20) % 10) // 5,
        (((money % 50) % 20) % 10) % 5
    )
    print(sum(coins))
    result = "50 " * coins[0] + "20 " * coins[1] + "10 " * coins[2] + "5 " * coins[3] + "1 " * coins[4]
    print(result.rstrip())


if __name__ == "__main__":
    main()
