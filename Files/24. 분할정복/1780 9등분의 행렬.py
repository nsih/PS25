import sys

def sol(r, c, n):
    global minusCnt
    global plusCnt
    global zeroCnt

    num = tree[r][c]

    for i in range(r, r + n):
        for j in range(c, c + n):
            if tree[i][j] != num:
                p1 = n // 3
                p2 = (n // 3) * 2

                sol(r, c, p1)
                sol(r+p1, c, p1)
                sol(r+p2, c, p1)

                sol(r, c+p1, p1)
                sol(r+p1, c+p1, p1)
                sol(r+p2, c+p1, p1)

                sol(r, c+p2, p1)
                sol(r+p1, c+p2, p1)
                sol(r+p2, c+p2, p1)
                return

    if num == -1:
        minusCnt += 1
    elif num == 1:
        plusCnt += 1
    else:
        zeroCnt += 1


n = int(sys.stdin.readline())
tree = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]

minusCnt = 0
zeroCnt = 0
plusCnt = 0

sol(0, 0, n)

print(minusCnt)
print(zeroCnt)
print(plusCnt)