import sys

n = int(sys.stdin.readline())
lst = []

for _ in range(n):
	lst.append(list(map(int, sys.stdin.readline().split())))

lst.sort(key=lambda x: (x[1], x[0]))

cnt = 1
e = lst[0][1]

for i in range(1, len(lst)):
	if lst[i][0] >= e:
		cnt += 1
		e = lst[i][1]

print(cnt)