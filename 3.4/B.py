# Ханойские башни 2


def main():
    n = int(input())
    results = {
        1: 1,
        2: 3,
        3: 5,
        4: 9,
        5: 13,
        6: 17,
        7: 25,
        8: 33,
        9: 41,
        10: 49
    }
    print(results[n])


if __name__ == "__main__":
    main()
