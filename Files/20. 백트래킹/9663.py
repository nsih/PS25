import sys

def nq(row):
    global res

    if row == n:
        res += 1
        return

    for col in range(n):
        if col not in cols and (row+col) not in diags1 and (row-col) not in diags2:
            cols.add(col)
            diags1.add(row + col)
            diags2.add(row - col)

            nq(row+1)

            diags2.remove(row - col)
            diags1.remove(row + col)
            cols.remove(col)

    return True

n = int(sys.stdin.readline())
cols = set()
diags1 = set()
diags2 = set()

res = 0
nq(0)

print(res)