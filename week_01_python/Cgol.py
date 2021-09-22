import random

def createNewBoard(rows,cols):
    board = [ [ 0 for i in range(rows) ] for j in range(cols) ]
    return board

def printBoard(board):
    for row in board:
        print(row)

def setCell(board, r, c, val):
    board[r][c] = val

def setBoard(board, numCells):
    for i in range(numCells):
        randomRow = random.randint(0, len(board)-1)
        randomCell = random.randint(0, len(board[0])-1)
        board[randomRow][randomCell] = 1
    return board

def countNeighbours(board, r, c):
    val = board[r][c]
    sumCellValues = 0
    for rowOffset in range(-1,2):
        for cellOffset in range(-1,2):
            if(rowOffset != 0 or cellOffset != 0):
                sumCellValues = sumCellValues + isCellAlive(board, r+rowOffset, c+cellOffset)
    return sumCellValues

def isCellAlive(board, r, c):
    if(r < 0 or r > len(board)-1):
        return 0
    elif(c < 0 or c > len(board[0])-1):
        return 0
    elif(board[r][c] == 1):
        return 1
    else:
        return 0

def getNextGenCell(board, r, c):
    val = countNeighbours(board, r, c)
    newVal = 0
    if(val <= 1):
        newVal = 0
    elif(val >= 4):
        newVal = 0
    elif(val == 2 or val == 3):
        newVal = 1
    else:
        if(val == 3):
            newVal = 1
    return newVal

def generateNextBoard(board):
    newBoard = [ [ 0 for i in range(len(board)) ] for j in range(len(board[0])) ]
    for row in range(0, len(board)):
        for cell in range(0, len(board[0])):
            newBoard[row][cell] = getNextGenCell(board, row, cell)
    return newBoard

gameBoard = createNewBoard(5,5)
setBoard(gameBoard,12)
for generations in range(0,5):
    print(" ")
    print("Gen " + str(generations+1) + ": ")
    printBoard(gameBoard)
    print("--------------------------")
    gameBoard = generateNextBoard(gameBoard)
