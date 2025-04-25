# Наименьшее общее кратное


def LCM(a: int, b: int) -> int:
    return (a * b) // GCD(a, b)


def GCD(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return max(a, b)
    return GCD(b, a % b)


def main():
    a, b = map(int, input().split())
    print(LCM(a, b))
    

if __name__ == "__main__":
    main()
