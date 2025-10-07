#a,b,c = map(int, input().split())
import sys

n,m = map(int,sys.stdin.readline().split())

lst = [i+1 for i in range(n)]

for _ in range(m):
    a,b = map ( int ,sys.stdin.readline().split())
    a -= 1
    b -= 1

    lst[a],lst[b] = lst[b],lst[a]

print(*lst)