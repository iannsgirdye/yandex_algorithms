# Бронирование переговорки
    

def main():
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
    
    data.sort(key=lambda x: x[1])
    result, min_end = 0, 0
    for i in range(n):
        if min_end < data[i][0]:
            min_end = data[i][1]
            result += 1
    
    print(result)


if __name__ == "__main__":
    main()
