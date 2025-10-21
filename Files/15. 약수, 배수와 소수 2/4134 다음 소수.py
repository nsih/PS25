import sys

def isP(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    if n == 0 or n == 1:
        print(2)

    else:
        while True:
            if isP(n):
                break
            else:
                n += 1
        print(n)
        
        
#단일 소수 판별 함수는 이게 맞다