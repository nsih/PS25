#a,b,c = map(int, input().split())
import sys


for l in sys.stdin:
    a, b = map(int, l.split())
    print(a + b)

#파이참 EOF는 ctrl+D