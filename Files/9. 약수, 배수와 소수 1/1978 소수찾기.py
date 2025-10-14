import sys

n = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split()))

temp = 0

for i in lst:
    if i == 1:
        temp += 1
        continue
    for j in range(2, int(i**0.5)+1) :
        if i%j == 0:
            temp += 1
            break

print(len(lst)-temp)