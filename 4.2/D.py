# A+B матрицы


def main():
    n, m = map(int, input().split())
    matrix1 = [list(map(int, input().split())) for x in range(n)]
    matrix2 = [list(map(int, input().split())) for y in range(n)]
    for i in range(n):
        for j in range(m):
            print(matrix1[i][j] + matrix2[i][j], end=" ")
        print()


if __name__ == "__main__":
    main()
