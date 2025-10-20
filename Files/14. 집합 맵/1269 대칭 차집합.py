import sys

str = sys.stdin.readline().strip()

lst = set()
for i in range(0, len(str)):
    for j in range(i,len(str)):
        lst.add(str[i:j+1])

print(len(lst))