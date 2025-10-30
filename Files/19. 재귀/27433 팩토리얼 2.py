import sys

def fectorial(n):
	if n > 1:
		return fectorial(n-1) * n
	else:
		return 1

n = int(sys.stdin.readline())
print(fectorial(n))