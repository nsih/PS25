import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]

tempWStandard = 0
minSC = 64

for i in range(n - 7):
    for j in range(m - 7):
        tempWStandard = 0

        for row in range(i,i+8):
            for col in range(j,j+8):
                #B틀림
                if row%2 == 0 and col%2 == 0 and board[row][col] == 'B':
                    tempWStandard += 1
                elif row %2 == 1 and col %2 ==1 and board[row][col] == 'B':
                    tempWStandard += 1
                #W틀림
                elif row%2 == 0 and col%2 == 1 and board[row][col] == 'W':
                    tempWStandard +=1
                elif row % 2 == 1 and col % 2 == 0 and board[row][col] == 'W':
                    tempWStandard += 1

        minSC = min(minSC,tempWStandard, 64-tempWStandard)

print(minSC)