import sys

def sol(r, c, n):
    color = tree[r][c]  # tree[행][열] -> tree[세로][가로]

    for i in range(r, r + n):
        for j in range(c, c + n):
            if tree[i][j] != color:
                print('(', end='')
                half = n // 2

                sol(r, c, half)
                sol(r, c + half, half)
                sol(r + half, c, half)
                sol(r + half, c + half, half)

                print(')', end='')
                return

    if color == '0':
        print('0', end='')
    else:
        print('1', end='')


n = int(sys.stdin.readline())
tree = [list(sys.stdin.readline().strip()) for _ in range(n)]

sol(0, 0, n)