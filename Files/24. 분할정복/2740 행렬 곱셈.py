import sys

n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

m2, k = map(int, sys.stdin.readline().split())
b = [list(map(int, sys.stdin.readline().split())) for _ in range(m2)]

result = [[0] * k for _ in range(n)]

for r in range(n):
    for c in range(k):
        for i in range(m):
            result[r][c] += a[r][i] * b[i][c]

for row in result:
    print(*(row))