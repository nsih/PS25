import sys

b = int(sys.stdin.readline())
a = [[1,1],[1,0]]

def mul(matrix1, matrix2):
    res = [[0] * 2 for _ in range(2)]
    for r in range(2):
        for c in range(2):
            for i in range(2):
                res[r][c] = (res[r][c] + matrix1[r][i] * matrix2[i][c]) % 1000000007
    return res


def power(matrix, exponent):
    if exponent == 1:
        for r in range(2):
            for c in range(2):
                matrix[r][c] %= 1000000007
        return matrix

    temp = power(matrix, exponent // 2)

    if exponent % 2 == 0:
        return mul(temp, temp)
    else:
        return mul(mul(temp, temp), matrix)

ans = power(a, b)

print(ans[0][1])
