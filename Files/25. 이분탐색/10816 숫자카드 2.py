import sys
from bisect import bisect_left, bisect_right, bisect

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())
tlst = list(map(int,sys.stdin.readline().split()))

lst.sort()

for t in tlst:
    print(bisect_right(lst, t) - bisect_left(lst, t), end=' ')