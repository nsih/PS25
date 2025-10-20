import sys

n,m = map(int, sys.stdin.readline().split())

lst1 = { sys.stdin.readline().strip() for _ in range(n)}
lst2 = { sys.stdin.readline().strip() for _ in range(m)}

result = sorted( lst1 & lst2 )

print(len(result))

for i in result:
    print(i)