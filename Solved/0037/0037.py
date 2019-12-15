# Problem No.: 37
# Solver:      Jinmin Goh
# Date:        20191215
# URL: https://leetcode.com/problems/sudoku-solver/

import sys

class Solution(object):
    def solveSudoku(self, board):
        self.board = board
        self.solve()
        
    def solve(self):
        row, col = self.getLine()
        if row == -1 and col == -1:
            return True
        for k in range(1,10):
            if self.isValidSudoku(row, col, str(k)):
                self.board[row][col] = str(k)
                if self.solve():
                    return True
                self.board[row][col] = '.'

    def getLine(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    return i,j
        return -1, -1
    
    def isValidSudoku(self, row, col, num):
        # row check
        if num in self.board[row]:
            return False
        # column check
        for i in range(9):
            if self.board[i][col] == num:
                return False
        # box check
        for i in range(3):
            for j in range(3):
                if self.board[(row // 3) * 3 + i][(col // 3) * 3 + j] == num:
                    return False
        return True
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        