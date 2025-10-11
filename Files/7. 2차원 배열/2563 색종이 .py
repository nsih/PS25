#import string
import sys

n = int(sys.stdin.readline())

lst = list([0]*100 for _ in range(100))

cnt = 0

for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())

    for i in range(10):
        for j in range(10):
            if lst[x+i][y+j] != 1:
                lst[x + i][y + j] = 1
                cnt +=1

print(cnt)