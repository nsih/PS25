#a,b,c = map(int, input().split())
import sys

t = int(sys.stdin.readline())

for i in range(t):
    a, b= map(int, input().split())

    print(f'Case #{i+1}: {a} + {b} = {a+b}')