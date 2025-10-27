import sys
from collections import Counter

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))

#
print(round(sum(lst) / n))

#
lst.sort()
print(lst[n // 2])

#
counts = Counter(lst)
modes = counts.most_common()

max_f = modes[0][1]
max_flst = []

for mode, freq in modes:
    if freq == max_f:
        max_flst.append(mode)
    else:
        break

max_flst.sort()

if len(max_flst) > 1:
    print(max_flst[1])
else:
    print(max_flst[0])

#
print(lst[-1] - lst[0])