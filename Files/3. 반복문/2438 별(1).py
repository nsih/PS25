#a,b,c = map(int, input().split())
import sys

t = int(sys.stdin.readline())

for i in range(t):
    for j in range(i+1):
        print('*',end='')
    print('')
