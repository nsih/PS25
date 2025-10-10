#a,b,c = map(int, input().split())
#import string
import sys

s = str(sys.stdin.readline().strip().upper())

lst = [0 for _ in range(26)]

for c in s:
    lst[ord(c) - ord('A')] += 1

if lst.count(max(lst)) >= 2:
    print('?')
else:
    print(chr(lst.index(max(lst)) + ord('A')))