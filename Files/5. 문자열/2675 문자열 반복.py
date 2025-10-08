#a,b,c = map(int, input().split())
#import string
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    r,s = map(str,sys.stdin.readline().strip().split())
    r = int(r)

    temp = "".join([c*r for c in s])

    temp = [c*r for c in s]
    print(temp)