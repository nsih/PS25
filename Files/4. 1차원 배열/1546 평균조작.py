#a,b,c = map(int, input().split())
import sys

n = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split()))

m = max(lst)

for i in range(len(lst)):
    lst[i] = (lst[i]/m)*100

print( sum(lst) / len(lst) )