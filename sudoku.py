grid = [[5,0,9, 0,0,0, 4,0,0],
        [7,0,8, 3,0,4, 9,0,0],
        [6,0,1, 0,0,0, 7,0,0],
        [4,6,2, 5,0,0, 0,0,0],
        [3,8,5, 7,2,0, 6,4,9],
        [1,0,7, 4,0,8, 2,0,0],
        [2,0,0, 1,0,0, 0,0,4],
        [0,0,3, 0,4,0, 0,8,7],
        [0,7,0, 0,5,3, 0,0,6]] # input the board

def getBoard(grid): # print the board 
    for row in range(len(grid)): # iterate through rows (vertically)
        if row % 3 == 0 and row != 0: # if multiple of 3 and not zero, print line
            print('- - - - - - - - - - -')
        for col in range(len(grid[0])): # iterate through columns (horizontally)
            if col % 3 == 0 and col != 0:
                print('|', end = ' ')
            if col == 8: # print values on their squares
                print(grid[row][col])
            else:
                print(grid[row][col], end=' ')

def findEmpty(grid): # find empty space
    for row in range(len(grid)): 
        for col in range(len(grid[0])): 
            if grid[row][col] == 0:
                return (row, col)
    
    return None

def checkIfValid(grid, row, col, val): # check if the guess is possibly correct
    # for rowEntry in range(9): # iterate through the row values
    #     if grid[row][rowEntry] == val: # and col != rowEntry:
    #         return False
    for rowEntry in grid[row]:
        if rowEntry == val:
            return False
    
    # for colEntry in range(9): # iterate through col values
    #     if grid[colEntry][col] == val: # and row != colEntry:
    #         return False
    for colEntry in (grid[row][col] for row in range(9)):
        if colEntry == val:
            return False
    
    rowStart = (row // 3) * 3
    colStart = (col // 3) * 3
    for i in range(rowStart, rowStart + 3):
        for j in range(colStart, colStart + 3):
            if grid[i][j] == val and (i,j) != (row,col):
                return False
    
    return True

def solveSudoku(grid):
    emptySquare = findEmpty(grid)
    if emptySquare == None:
        return True
    else:
        row, col = emptySquare

    for guess in range(1, 10):
        if checkIfValid(grid, row, col, guess):
            grid[row][col] = guess

            if solveSudoku(grid):
                return True
        
            grid[row][col] = 0

    return False

getBoard(grid)
if solveSudoku(grid) == False:
    print('Board is unsolvable')
else:
    print('____________________________________________')
    getBoard(grid)
