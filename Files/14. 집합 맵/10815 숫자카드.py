import sys

_ = sys.stdin.readline()
lst1 = set(map(int,sys.stdin.readline().split()))
_ = sys.stdin.readline()
lst2 = list(map(int,sys.stdin.readline().split()))

lst3 = []

for i in lst2:
    if i in lst1:
        lst3.append(1)
    else:
        lst3.append(0)

print(*lst3)