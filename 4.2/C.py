# A+B строки


def main():
    n = int(input())
    str1 = input()
    str2 = input()
    str12 = ""
    for i in range(n):
        str12 += str1[i] + str2[i]
    print(str12)
    
    
if __name__ == "__main__":
    main()
