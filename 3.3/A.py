# Камни


from functools import lru_cache


@lru_cache
def game(n: int, m: int) -> str:
    if n == 0 and m == 0:
        return "Lose"
    if n <= 1 and m <= 1:
        return "Win"
    if n == 0:
        if game(n, m - 1) == "Lose":
            return "Win"
        return "Lose"
    if m == 0:
        if game(n - 1, m) == "Lose":
            return "Win"
        return "Lose"
    if any(x == "Lose" for x in [game(n - 1, m), game(n - 1, m - 1), game(n, m - 1)]):
        return "Win"
    return "Lose"


def main():
    n, m = map(int, input().split())
    print(game(n, m))


if __name__ == "__main__":
    main()
