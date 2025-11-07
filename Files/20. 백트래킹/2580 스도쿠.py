import sys


def dfs(depth):
    if depth == 81:
        return True

    r = depth // 9
    c = depth % 9

    if sudoku[r][c] != 0:
        return dfs(depth + 1)

    else:
        for n in range(1, 10):
            if validSudoku(r, c, n):
                sudoku[r][c] = n
                if dfs(depth + 1):
                    return True
                sudoku[r][c] = 0
        return False


def validSudoku(r, c, num):
    for i in range(9):
        if sudoku[r][i] == num:
            return False

    for i in range(9):
        if sudoku[i][c] == num:
            return False

    start_r = (r // 3) * 3
    start_c = (c // 3) * 3
    for i in range(start_r, start_r + 3):
        for j in range(start_c, start_c + 3):
            if sudoku[i][j] == num:
                return False

    return True


sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().split())))

dfs(0)

for row in sudoku:
    print(*row)

# (0,0)~(2,2) | (0,3)~(2,5) | (0,6)~(2,8)
# -------------+-------------+-------------
# (3,0)~(5,2) | (3,3)~(5,5) | (3,6)~(5,8)
# -------------+-------------+-------------
# (6,0)~(8,2) | (6,3)~(8,5) | (6,6)~(8,8)

# sr = (r//3)*3
# sc = (c//3)*3
# for i in range(sr, sr+3):
#    for j in range(sc, sc+3):
#        if sudoku[i][j] == num:
#            return False