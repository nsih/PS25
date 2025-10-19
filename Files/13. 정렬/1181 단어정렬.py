import sys

n = int(sys.stdin.readline())

lst = {sys.stdin.readline().strip() for _ in range(n)}

lst = sorted(lst,key=lambda  x : (len(x),x))

for i in lst:
    print(i)