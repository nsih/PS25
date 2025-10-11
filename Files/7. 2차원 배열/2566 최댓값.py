#import string
import sys

lst = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]

lst2 = []
for row in lst:
    lst2.append(max(row))

maxLst = max(lst2)
maxRowIdx = lst2.index(maxLst)
maxColIdx = lst[maxRowIdx].index(maxLst)

print(maxLst)
print(maxRowIdx+1, maxColIdx+1)


#enumerate
lst = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]

lst2 = []
for row in lst:
    lst2.append(max(row))

max_val = -1

max_row = -1
max_col = -1

for r,row in enumerate(lst):
    for c, val in enumerate(row):
        if val > max_val:
            max_val = val
            max_row = r
            max_col = c

print(max_val)
print(max_row+1,max_col+1)