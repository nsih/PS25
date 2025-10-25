from collections import deque
import sys

t = int(sys.stdin.readline())
deck = deque()

for _ in range(t):
    cmds = sys.stdin.readline().split()
    cmd = int(cmds[0])

    if cmd == 1:
        deck.appendleft(int(cmds[1]))

    elif cmd == 2:
        deck.append(int(cmds[1]))

    elif cmd == 3:
        if len(deck):
            print(deck.popleft())
        else:
            print(-1)

    elif cmd == 4:
        if len(deck):
            print(deck.pop())
        else:
            print(-1)

    elif cmd == 5:
        print(len(deck))

    elif cmd == 6:
        if len(deck):
            print(0)
        else:
            print(1)

    elif cmd == 7:
        if len(deck):
            print(deck[0])
        else:
            print(-1)

    elif cmd == 8:
        if len(deck):
            print(deck[-1])
        else:
            print(-1)