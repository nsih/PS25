#a,b,c = map(int, input().split())
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    s = str(sys.stdin.readline().rstrip())
    print(f'{s[0]}{s[-1]}')
