import sys

n, b = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def mul(matrix1, matrix2):
    res = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            for i in range(n):
                res[r][c] = (res[r][c] + matrix1[r][i] * matrix2[i][c]) % 1000
    return res


def power(matrix, exponent):
    if exponent == 1:
        for r in range(n):
            for c in range(n):
                matrix[r][c] %= 1000
        return matrix

    temp = power(matrix, exponent // 2)

    if exponent % 2 == 0:
        return mul(temp, temp)
    else:
        return mul(mul(temp, temp), matrix)

ans = power(a, b)

# 결과 출력
for row in ans:
    print(*(row))