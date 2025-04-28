#Backtracking:
N = int(input("N = "))
empty = '-'
queen = 'Q'
b = [[empty] * N for i in range(N)]

def isSafe(i, j):
    for p in range(N):
        if b[p][j] == queen or b[i][p] == queen:
            return False
    for n in range(N):
        for m in range(N):
            if i + j == n + m or i - j == n - m:
                if b[n][m] == queen:
                    return False
    return True

def nqueen(noq):
    if noq == 0:
        return True
    for i in range(N):
        for j in range(N):
            if b[i][j] != queen and isSafe(i, j):
                b[i][j] = queen
                if nqueen(noq - 1):
                    return True
                b[i][j] = empty
    return False

def printBoard(b):
    for i in b:
        for j in i:
            print(j, end = " ")
        print()

if nqueen(N): 
    printBoard(b)
else:
    print("Can't place")



#Branch and bound:
N = int(input("N = "))
empty = '-'
queen = 'Q'
b = [[empty] * N for i in range(N)]

def isSafe(board, row, col, n):
    for i in range(row):
        if board[i][col] == queen:
            return False
        if (col - (row - i)) >= 0 and board[i][col - (row - i)] == queen:
            return False
        if (col + (row - i)) < n and board[i][col + (row - i)] == queen:
            return False
    return True

def branch_and_bound(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = queen
            if branch_and_bound(board, row + 1, n):
                return True
            board[row][col] = empty
    return False

def printBoard(board):
    for i in board:
        for j in i:
            print(j, end = " ")
        print()

if branch_and_bound(b, 0, N):
    printBoard(b)
else:
    print("Can't place")
