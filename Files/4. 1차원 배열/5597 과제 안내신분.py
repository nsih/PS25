#a,b,c = map(int, input().split())
import sys


lst = [i+1 for i in range(30)]

for _ in range(28):
    lst.remove(int(sys.stdin.readline()))

for i in lst:
    print(i)