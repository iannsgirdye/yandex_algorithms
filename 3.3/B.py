# Камни 2
"""
/0123456
0LWWLWWL
1WLWWLWW
2WWLWWLW
3LWWLWWL
"""


def game(n: int, m: int) -> str:
    if (n % 3) == (m % 3):
        return "Lose"
    return "Win"


def main():
    n, m = map(int, input().split())
    print(game(n, m))
    
    
if __name__ == "__main__":
    main()
