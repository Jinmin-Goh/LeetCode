# Problem No.: 289
# Solver:      Jinmin Goh
# Date:        20200316
# URL: https://leetcode.com/problems/game-of-life/

import sys

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        newBoard = [[0] * len(board[0]) for i in range(len(board))]
        nrow = len(board)
        ncol = len(board[0])
        if nrow == 1 or ncol == 1:
            for i in range(nrow):
                for j in range(ncol):
                    board[i][j] = newBoard[i][j]
            return
        for i in range(nrow):
            for j in range(ncol):
                # 4 points
                if i == 0 and j == 0:
                    temp = board[i + 1][j] + board[i][j + 1] + board[i + 1][j + 1]
                elif i == 0 and j == ncol - 1:
                    temp = board[i + 1][j] + board[i][j - 1] + board[i + 1][j - 1]
                elif i == nrow - 1 and j == 0:
                    temp = board[i - 1][j] + board[i][j + 1] + board[i - 1][j + 1]
                elif i == nrow - 1 and j == ncol - 1:
                    temp = board[i - 1][j] + board[i][j - 1] + board[i - 1][j - 1]
                # edges
                elif i == 0:
                    temp = board[i + 1][j] + board[i][j + 1] + board[i + 1][j + 1] + board[i + 1][j - 1] + board[i][j - 1]
                elif i == nrow - 1:
                    temp = board[i - 1][j] + board[i][j + 1] + board[i - 1][j + 1] + board[i - 1][j - 1] + board[i][j - 1]
                elif j == 0:
                    temp = board[i + 1][j] + board[i][j + 1] + board[i + 1][j + 1] + board[i - 1][j] + board[i - 1][j + 1]
                elif j == ncol - 1:
                    temp = board[i + 1][j] + board[i][j - 1] + board[i + 1][j - 1] + board[i - 1][j] + board[i - 1][j - 1]
                # insiders
                else:
                    temp = board[i + 1][j] + board[i][j + 1] + board[i - 1][j] + board[i][j - 1] + board[i + 1][j + 1] + board[i + 1][j - 1] + board[i - 1][j + 1] + board[i - 1][j - 1]
                if board[i][j] == 1:               
                    if 2 <= temp <= 3:
                        newBoard[i][j] = 1
                    else:
                        newBoard[i][j] = 0
                else:
                    if temp == 3:
                        newBoard[i][j] = 1
        for i in range(nrow):
            for j in range(ncol):
                board[i][j] = newBoard[i][j]