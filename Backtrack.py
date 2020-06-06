"""Created 6/4/20 by Isaac Stong
Algorithm that solves Sodoku board"""
import numpy as np
import Backtrack_func as bf


def solve_board(board):
    empty = bf.find_0(board)
    if not empty:
        return True
    else:
        row, col = empty
    for i in range(1,10):
        if bf.is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve_board(board):
                return True

            board[row][col] = 0

    return False



