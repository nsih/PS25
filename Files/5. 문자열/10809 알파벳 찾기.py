#a,b,c = map(int, input().split())
#import string
import sys

s = str(sys.stdin.readline().strip())

alp = [-1 for i in range(26)]

for i in range(len(s)):
    if alp[ord(s[i])-97] == -1:
        alp[ord(s[i])-97] = i

print(*alp)