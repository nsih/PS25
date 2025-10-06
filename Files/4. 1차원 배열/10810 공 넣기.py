#a,b,c = map(int, input().split())
import sys

n,m = map(int,sys.stdin.readline().split())

lst = [0 for _ in range(n)]

for _ in range(m):
    i,j,k = map ( int ,sys.stdin.readline().split())

    for l in range(i,j+1):
        lst[l-1] = k

print(*lst)