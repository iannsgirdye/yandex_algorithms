# A(x) + B(x)


def to_int(number: str) -> int:
    return int(number.replace(" ", ""))
        

def main():
    n1, int1 = input(), to_int(input())
    n2, int2 = input(), to_int(input())
    
    int12 = str(int1 + int2)
    n12 = len(int12) - 1
    
    print(n12)
    for i in int12:
        print(i, end=" ")


if __name__ == "__main__":
    main()
