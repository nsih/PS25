import sys

n = int(sys.stdin.readline())

lst = []

for i in range(n):
    age, name = sys.stdin.readline().strip().split()
    lst.append((age,name,i))

lst = sorted(lst, key = lambda x : (int(x[0]), x[2]))

for i in lst:
    print(i[0],i[1])