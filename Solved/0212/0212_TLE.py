# Problem No.: 212
# Solver:      Jinmin Goh
# Date:        20200308
# URL: https://leetcode.com/problems/word-search-ii/

import sys

# 34/36 passed and TLE

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        wordDict = {}
        for i in words:
            if i[0] not in wordDict:
                wordDict[i[0]] = [i]
            else:
                wordDict[i[0]].append(i)
        ans = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in wordDict:
                    for word in wordDict[board[i][j]]:
                        tempBoard = [_[:] for _ in board]
                        if self.DFS(word, i, j, 0, tempBoard):
                            ans.append(word)
                            wordDict[board[i][j]].pop(wordDict[board[i][j]].index(word))
        return ans
        
    def DFS(self, word: str, row: int, col: int, cnt: int, board: List[List[str]]) -> bool:
        # word found
        if cnt >= len(word):
            return True
        if not (0 <= row < len(board)) or not (0 <= col < len(board[0])) or board[row][col] == ".":
            return False
        if word[cnt] == board[row][col]:
            #print(word, cnt, word[cnt], row, col)
            tempBoard = [_[:] for _ in board]
            tempBoard[row][col] = "."
            flag = False
            flag = flag or self.DFS(word, row + 1, col, cnt + 1, tempBoard)
            flag = flag or self.DFS(word, row - 1, col, cnt + 1, tempBoard)
            flag = flag or self.DFS(word, row, col + 1, cnt + 1, tempBoard)
            flag = flag or self.DFS(word, row, col - 1, cnt + 1, tempBoard)
            return flag
        else:
            return False