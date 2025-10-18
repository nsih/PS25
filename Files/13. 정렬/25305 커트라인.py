import sys

n,k = map(int,sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))

lst = sorted(lst)

print(lst[n-k])