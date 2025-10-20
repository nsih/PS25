import sys

n = int(sys.stdin.readline())

lst = set()

for _ in range(n):
    name, log = map(str, sys.stdin.readline().strip().split())
    if log == 'enter':
        lst.add(name)
    else:
        lst.remove(name)


result = sorted(lst,reverse = True)

for i in result:
    print(i)