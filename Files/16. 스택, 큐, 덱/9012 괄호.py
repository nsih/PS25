import sys

t = int(sys.stdin.readline())

res = []

for _ in range(t):
    lst = sys.stdin.readline().strip()

    stack = []
    ok = True

    for c in lst:
        if c == '(':
            stack.append( '(' )

        else:
            if stack:
                stack.pop()
            else:
                ok = False
                break

    res.append('YES' if ok and not stack else 'NO')


print('\n'.join(res))