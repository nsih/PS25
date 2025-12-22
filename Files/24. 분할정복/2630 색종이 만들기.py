import sys

def sol(x,y,n):
    color = paper[x][y]

    global whiteCnt, blueCnt
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j] != color:
                half = n//2
                sol(x + half, y, half)      #1사분면
                sol(x, y, half)             #2사분면
                sol(x, y + half, half)      #3사분면
                sol(x + half, y + half, half)   #4사분면
                return

    if color == 0:
        whiteCnt += 1
    else:
        blueCnt += 1


n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

whiteCnt = 0
blueCnt = 0

sol(0,0,n)

print(whiteCnt)
print(blueCnt)

