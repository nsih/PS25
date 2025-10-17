import sys

n = int(sys.stdin.readline())
temp = 1
i = 666

while temp != n:
    i += 1
    if '666' in str(i):
        temp+=1
print(i)