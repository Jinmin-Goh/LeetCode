# Problem No.: 212
# Solver:      Jinmin Goh
# Date:        20200308
# URL: https://leetcode.com/problems/word-search-ii/

import sys

# used Trie
# implemented from https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:
    def __init__(self):
        self.wordSet = set()
        self.prefixSet = set()

    def insert(self, word: str) -> None:
        self.wordSet.add(word)
        for i in range(len(word)):
            if word[:i + 1] not in self.prefixSet:
                self.prefixSet.add(word[:i + 1])
        
    def search(self, word: str) -> bool:
        return word in self.wordSet

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefixSet


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordTrie = Trie()
        for i in words:
            wordTrie.insert(i)
        self.ans = []
        self.ansSet = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                tempBoard = [_[:] for _ in board]
                self.DFS(i, j, "", tempBoard, wordTrie)
        return self.ans
        
    def DFS(self, row: int, col: int, path: str, board: List[List[str]], wordTrie: Trie) -> None:
        # word found
        if wordTrie.search(path) and path not in self.ansSet:
            self.ans.append(path)
            self.ansSet.add(path)
            return
        if not (0 <= row < len(board)) or not (0 <= col < len(board[0])) or board[row][col] == ".":
            return
        if path and not wordTrie.startsWith(path):
            return
        temp = board[row][col]
        board[row][col] = "."
        flag = False
        flag = flag or self.DFS(row + 1, col, path + temp, board, wordTrie)
        flag = flag or self.DFS(row - 1, col, path + temp, board, wordTrie)
        flag = flag or self.DFS(row, col + 1, path + temp, board, wordTrie)
        flag = flag or self.DFS(row, col - 1, path + temp, board, wordTrie)
        board[row][col] = temp