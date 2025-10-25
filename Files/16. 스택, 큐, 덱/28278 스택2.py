import sys

n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    inputValue = sys.stdin.readline().split()
    cmd = int(inputValue[0])

    if cmd == 1:
        stack.append( inputValue[1] )

    elif cmd == 2:
        if len(stack):
            print(stack.pop())
        else:
            print(-1)

    elif cmd == 3:
        print(len(stack))

    elif cmd ==4:
        if len(stack):
            print(0)
        else:
            print(1)

    elif cmd == 5:
        if len(stack):
            print(stack[-1])
        else:
            print(-1)