import sys

pairs = {')': '(', ']': '['}

for line in sys.stdin:
    s = line.rstrip('\n')

    if s == '.':
        break

    stack = []
    ok = True

    for c in s:
        if c in '([':
            stack.append(c)
        elif c in ')]':
            if stack and stack[-1] == pairs[c]:
                stack.pop()
            else:
                ok = False
                break

    print('yes' if ok and not stack else 'no')
