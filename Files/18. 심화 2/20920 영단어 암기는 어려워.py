import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())

dic = []

for _ in range(n):
    w = sys.stdin.readline().strip()

    if len(w) >= m:
        dic.append(w)

counts = Counter(dic)

sdic = sorted(counts.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in sdic:
    print(i[0])