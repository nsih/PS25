import sys


def nq(row):  # queen count
    if row == n:
        return 1

    cnt = 0
    for col in range(n):
        if (col in cols) or (row + col in diag1) or (row - col in diag2):
            continue

        cols.add(col)
        diag1.add(row + col)
        diag2.add(row - col)

        cnt += nq(row + 1)

        cols.remove(col)
        diag1.remove(row + col)
        diag2.remove(row - col)

    return cnt


n = int(sys.stdin.readline())

cols = set()  # 열
diag1 = set()  # 대각1
diag2 = set()  # 대각2

print(nq(0))