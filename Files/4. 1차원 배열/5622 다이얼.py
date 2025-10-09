#a,b,c = map(int, input().split())
#import string
import sys

lst = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]

s = str(sys.stdin.readline().strip())

temp = 0
for c in s:
    temp += lst[ord(c)-ord('A')]

print(temp)