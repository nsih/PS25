import sys


def star(lst):
    if len(lst) == 1:
        return lst

    d = len(lst) // 3

    lst0 = [row[0:d] for row in lst[0:d]]
    lst0 = star(lst0)
    lst1 = [row[d:d * 2] for row in lst[d:d * 2]]
    for i in range(d):
        for j in range(d):
            lst1[i][j] = ' '

    top_rows = [lst0[i] + lst0[i] + lst0[i] for i in range(d)]
    mid_rows = [lst0[i] + lst1[i] + lst0[i] for i in range(d)]
    bot_rows = [lst0[i] + lst0[i] + lst0[i] for i in range(d)]

    return top_rows + mid_rows + bot_rows


n = int(sys.stdin.readline())

lst = [['*'] * n for _ in range(n)]

res = star(lst)
print('\n'.join(''.join(row) for row in res))