import sys

n = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split()))

pc = 0

for i in lst:
    if i == 1:
        continue

    isP = True

    for j in range(2, int(i**0.5)+1) :
        if i%j == 0:
            isP = False
            break

    if isP:
        pc += 1

print(pc)