# Problem No.: 208
# Solver:      Jinmin Goh
# Date:        20200205
# URL: https://leetcode.com/problems/implement-trie-prefix-tree/

import sys

# list implementation
class Trie:

    def __init__(self):
        self.wordList = []

    def insert(self, word: str) -> None:
        self.wordList.append(word)
        
    def search(self, word: str) -> bool:
        if word in self.wordList:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        for i in self.wordList:
            if i[:len(prefix)] == prefix:
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)