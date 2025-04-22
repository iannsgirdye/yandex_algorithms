# Максимальное произведение — контрпример


def main():
    n = int(input())
    if n < 7:
        print("No")
    else:
        print("Yes")
        print(n, end=" ")
        for i in range(1, n):
            print(i, end=" ")


if __name__ == "__main__":
    main()
