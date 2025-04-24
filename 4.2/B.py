# A(x) + B(x)
        

def main():
    n1, int1 = int(input()), list(map(int, input().split()))
    n2, int2 = int(input()), list(map(int, input().split()))
    
    n12, int12 = max(n1, n2), []
    for i in range(-1, -n12 - 2, -1):
        if i < -n1 - 1:
            int12.append(int2[i])
        elif i < -n2 - 1:
            int12.append(int1[i])
        else:
            int12.append(int1[i] + int2[i])
    
    print(n12)
    print(*int12[::-1])


if __name__ == "__main__":
    main()
