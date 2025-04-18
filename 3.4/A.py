# Ханойские башни


def HanoiTowers(n: int, fromPeg: int, toPeg: int) -> None:
    if n == 1:
        print(fromPeg, toPeg)
        return
    unusedPeg = 6 - fromPeg - toPeg
    HanoiTowers(n - 1, fromPeg, unusedPeg)
    print(fromPeg, toPeg)
    HanoiTowers(n - 1, unusedPeg, toPeg)


def main():
    n = int(input())
    print(2 ** n - 1)
    HanoiTowers(n, 1, 3)
    

if __name__ == "__main__":
    main()
