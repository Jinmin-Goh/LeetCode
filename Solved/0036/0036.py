# Problem No.: 36
# Solver:      Jinmin Goh
# Date:        20191215
# URL: https://leetcode.com/problems/valid-sudoku/

import sys

class Solution(object):
    def isValidSudoku(self, board):
        hash_table = [False] * 9
        for i in range(9):
            row_table = hash_table[:]
            col_table = hash_table[:]
            box_table = hash_table[:]
            for j in range(9):
                # row check
                if board[i][j] != '.' and row_table[int(board[i][j]) - 1]:
                    return False
                elif board[i][j] != '.':
                    row_table[int(board[i][j]) - 1] = True
                # column check
                if board[j][i] != '.' and col_table[int(board[j][i]) - 1]:
                    return False
                elif board[j][i] != '.':
                    col_table[int(board[j][i]) - 1] = True
                # box check
                if board[3 * (i // 3) + j // 3][(i % 3) * 3 + j % 3] != '.' and box_table[int(board[3 * (i // 3) + j // 3][(i % 3) * 3 + j % 3]) - 1]:
                    return False
                elif board[3 * (i // 3) + j // 3][(i % 3) * 3 + j % 3] != '.':
                    box_table[int(board[3 * (i // 3) + j // 3][(i % 3) * 3 + j % 3]) - 1] = True
        return True
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        