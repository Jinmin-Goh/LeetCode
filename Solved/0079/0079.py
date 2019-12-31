# Problem No.: 79
# Solver:      Jinmin Goh
# Date:        20191231
# URL: https://leetcode.com/problems/word-search/

import sys

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word or not board:
            return False
        check_board = [[False] * len(board[0]) for i in range(len(board))]
        self.board = board
        validFlag = False
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                validFlag = self.search(i, j, check_board, word)
                if validFlag:
                    return True
        return False
        
    def search(self, i: int, j: int, check_board: List[List[str]], word: str) -> bool:
        #print(i, j, check_board, word)
        if self.board[i][j] != word[0]:
            return False  
        if self.board[i][j] == word[0]:
            temp_board = [_[:] for _ in check_board]
            temp_board[i][j] = True
            if len(word) == 1:
                return True
            if i > 0 and not check_board[i - 1][j]:
                if self.search(i - 1, j, temp_board[:], word[1:]):
                    return True
            if i < len(self.board) - 1 and not check_board[i + 1][j]:
                if self.search(i + 1, j, temp_board[:], word[1:]):
                    return True
            if j > 0 and not check_board[i][j - 1]:
                if self.search(i, j - 1, temp_board[:], word[1:]):
                    return True
            if j < len(self.board[0]) - 1 and not check_board[i][j + 1]:
                if self.search(i, j + 1, temp_board[:], word[1:]):
                    return True
            return False
        