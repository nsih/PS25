#import string
import sys

n,m = map(int,sys.stdin.readline().split())

lstA = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
lstB = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

lst = [[lstA[i][j]+lstB[i][j] for j in range(m)] for i in range(n)]

for row in lst:
    print(*row)