import sys

n = int(sys.stdin.readline())

b = False
fb = n//5
tb = 0

while fb >= 0:
    temp = n-(5*fb)

    if temp%3 != 0:
        fb -= 1
    else:
        tb = temp//3
        b = True
        break

if b:
    print(fb+tb)
else:
    print(-1)