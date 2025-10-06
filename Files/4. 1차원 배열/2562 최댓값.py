#a,b,c = map(int, input().split())
import sys

lst = [int(sys.stdin.readline()) for _ in range(9) ]

m = max(lst)
print(m)
print(lst.index(m)+1)