#a,b,c = map(int, input().split())
import sys

t = int(sys.stdin.readline())

for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)