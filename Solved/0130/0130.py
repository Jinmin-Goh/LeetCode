# Problem No.: 130
# Solver:      Jinmin Goh
# Date:        20200120
# URL: https://leetcode.com/problems/surrounded-regions/

import sys

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        self.nrow = len(board)
        self.ncol = len(board[0])
        # find O group of edge and change to other word
        for i in range(self.ncol):
            self.dfs(board, 0, i)
            self.dfs(board, self.nrow - 1, i)
        for i in range(self.nrow):
            self.dfs(board, i, 0)
            self.dfs(board, i, self.ncol - 1)
        # change remaining O to X and return exde O groups
        for i in range(self.nrow):
            for j in range(self.ncol):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == ".":
                    board[i][j] = "O"
            
    def dfs(self, board: List[List[str]], row: int, col: int) -> None:
        if row >= self.nrow or row < 0 or col >= self.ncol or col < 0:
            return
        if board[row][col] == "O":
            board[row][col] = "."
            self.dfs(board, row - 1, col)
            self.dfs(board, row + 1, col)
            self.dfs(board, row, col - 1)
            self.dfs(board, row, col + 1)