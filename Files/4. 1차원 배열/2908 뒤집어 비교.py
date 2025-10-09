#a,b,c = map(int, input().split())
#import string
import sys

a,b = map(str, sys.stdin.readline().split())

a_ = int(a[::-1])
b_ = int(b[::-1])

if a_ < b_:
    print(b_)
else:
    print(a_)