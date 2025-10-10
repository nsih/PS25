#a,b,c = map(int, input().split())
#import string
import sys

lst1 = [1,1,2,2,2,8]

lst2 = list(map(int,sys.stdin.readline().split()))

for i in range(len(lst1)):
    lst1[i]-=lst2[i]

print(*lst1)