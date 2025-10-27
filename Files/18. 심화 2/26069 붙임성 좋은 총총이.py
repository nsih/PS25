import sys

n = int(sys.stdin.readline())
s = set()
s.add('ChongChong')

for _ in range(n):
    s0,s1 = map(str,sys.stdin.readline().strip().split())
    if s0 in s or s1 in s:
        s.add(s0)
        s.add(s1)

print(len(s))