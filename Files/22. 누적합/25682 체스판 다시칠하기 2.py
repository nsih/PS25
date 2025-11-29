import sys

n,m,k = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(n) ]

psum = [[0]*(m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        if (i+j) % 2 == 0:
            if board[i][j] == 'B':
                value = 0
            else:
                value = 1
        else:
            if board[i][j] == 'B':
                value = 1
            else:
                value = 0

        psum[i+1][j+1] = psum[i][j+1] + psum[i+1][j] - psum[i][j] + value

msw = 1e9

for i in range(n-k+1):
    for j in range(m-k+1):
        sw = psum[i + k][j + k] - psum[i][j + k] - psum[i + k][j] + psum[i][j]
        msw = min(msw, sw, (k * k) - sw)

print(msw)