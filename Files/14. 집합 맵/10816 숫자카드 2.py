import sys
from collections import Counter

_ = sys.stdin.readline()
lst1 = list(map(int, sys.stdin.readline().split()))
_ = sys.stdin.readline()
lst2 = list(map(int, sys.stdin.readline().split()))

counts = Counter(lst1)

for i in lst2:
    print(counts[i], end=' ')