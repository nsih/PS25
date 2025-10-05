#a,b,c = map(int, input().split())
import sys

while(1):
    try:
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
    except ValueError :
        break


for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)