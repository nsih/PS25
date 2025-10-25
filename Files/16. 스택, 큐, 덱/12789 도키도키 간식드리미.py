import sys
input = sys.stdin.readline

n = int(input().strip())
lst = list(map(int, input().split()))

stack = []
temp = 1  # 지금 찾아야 하는 번호

for i in lst:
    while stack and stack[-1] == temp:
        stack.pop()
        temp += 1

    if i == temp:
        temp += 1
    else:
        stack.append(i)

while stack and stack[-1] == temp:
    stack.pop()
    temp += 1

print('Nice' if temp == n + 1 else 'Sad')
