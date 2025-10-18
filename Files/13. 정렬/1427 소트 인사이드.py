import sys

lst = sys.stdin.readline().strip()

lst = sorted(lst)

for i in range(len(lst)-1, -1, -1):
    print(lst[i],end='')