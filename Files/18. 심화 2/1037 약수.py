import sys

n = sys.stdin.readline()

lst = list(map(int,sys.stdin.readline().split()))

res = min(lst)*max(lst)

print(res)