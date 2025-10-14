import sys

n = int(sys.stdin.readline())

i,temp = 0,0

while True:
    i += 1
    if i == 1:
        if n == 1:
            break;

    else:
        temp = 6*(i-1) + temp
        if temp+1 >= n:
            break

print(i)