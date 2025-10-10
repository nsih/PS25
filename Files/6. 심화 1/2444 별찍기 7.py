#a,b,c = map(int, input().split())
#import string
import sys

n = int(sys.stdin.readline())

for i in range(n):
    print(' ' * (n-1-i) + '*' * (i*2+1))

for i in range(n-1):
    print(' ' * (i+1) + '*' * (n*2-((i+1)*2)-1))