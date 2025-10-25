import sys
from collections import deque

t = int(sys.stdin.readline())
q = deque()

res = []

for _ in range(t):
    cmds = sys.stdin.readline().split()
    cmd = cmds[0]

    if cmd == 'push':
        q.append(cmds[1])

    elif cmd == 'pop':
        if len(q):
            res.append(q.popleft())
        else:
            res.append(-1)

    elif cmd == 'size':
        res.append(len(q))

    elif cmd == 'empty':
        if len(q):
            res.append(0)
        else:
            res.append(1)

    elif cmd == 'front':
        if len(q):
            res.append(q[0])
        else:
            res.append(-1)

    elif cmd == 'back':
        if len(q):
            res.append(q[-1])
        else:
            res.append(-1)


print('\n'.join(map(str, res)))