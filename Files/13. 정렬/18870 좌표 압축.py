import sys

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

lst2 = sorted(set(lst))

dict = {lst2[i]: i for i in range(len(lst2))}

for i in lst:
    print(dict[i], end=' ')