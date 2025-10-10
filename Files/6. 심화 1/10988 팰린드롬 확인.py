#a,b,c = map(int, input().split())
#import string
import sys

s = str(sys.stdin.readline().strip())

if( s == s[::-1]):
    print(1)
else:
    print(0)