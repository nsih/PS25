import sys

n = int(sys.stdin.readline())
s = set()
temp = 0

for i in range(n):
    _str = sys.stdin.readline().strip()
    if  _str == 'ENTER':
        temp += len(s)
        s = set()

    else:
        s.add(_str)

print(len(s)+temp)