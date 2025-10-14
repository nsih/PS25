import sys


a,b,v = map(int,sys.stdin.readline().split())

if a >= v:
    print(1)
else:
    days = (v - a) // (a - b)

    if (v - a) % (a - b) != 0:
        days += 1

    print(days + 1)