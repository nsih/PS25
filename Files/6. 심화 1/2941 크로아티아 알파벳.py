#a,b,c = map(int, input().split())
#import string
import sys

s = str(sys.stdin.readline().strip())

lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for item in lst:
    s = s.replace(item,'+')

print(len(s))