import sys

n, m = map(int, sys.stdin.readline().split())

name_to_num = {}
num_to_name = {}

for i in range(1, n + 1):
    name = sys.stdin.readline().strip()
    name_to_num[name] = i
    num_to_name[i] = name

for _ in range(m):
    temp = sys.stdin.readline().strip()

    if temp.isdigit():
        print(num_to_name[int(temp)])
    else:
        print(name_to_num[temp])