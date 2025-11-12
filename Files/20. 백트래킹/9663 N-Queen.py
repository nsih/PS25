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


'''

같은 행은 안쓰니까 행(row)를 넘어가며 찾는다.

n이 row고 row 안에 col을 넣어서 체크 -> row 체크는 자동으로 할 필요 없어짐

cols,diag1,2 를 set으로 선언하고 매 행마다 (col in cols) or (row + col in diag1) or (row - col in diag2) 체크

넣으면 기록하고 다음행으로 넘어감

돌아오면 기록지우고 다음 열 체크


'''