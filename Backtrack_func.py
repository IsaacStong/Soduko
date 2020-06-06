"""Created by Isaac Stong 6/4/20
    Holds functions used in the main
    implementation of backtracking"""


#returns a space that needs to be solved for denoted by 0
def find_0(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return False


def is_valid(board, number, position):
    #Check row
    for i in range(len(board)):
        if board[position[0]][i] == number and position[1] != i:
            return False

    #Check col
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    #Check box
    x = position[1] // 3
    y = position[0] // 3
    for i in range(y * 3, y * 3 + 3):
        for j in range(x * 3, x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    return True
