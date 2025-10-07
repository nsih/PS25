#a,b,c = map(int, input().split())
import sys

n,m = map(int, sys.stdin.readline().split())

lst = [i+1 for i in range(n)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())

    start = i-1
    end = j

    lst[start:end] = reversed(lst[start:end])

print(*lst)