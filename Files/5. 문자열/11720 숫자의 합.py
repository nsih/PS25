#a,b,c = map(int, input().split())
import sys

n = int(sys.stdin.readline())

s = str(sys.stdin.readline().strip())

temp = 0
for i in range(n):
    temp += int(s[i])

print(temp)