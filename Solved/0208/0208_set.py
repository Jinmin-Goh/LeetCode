# Problem No.: 208
# Solver:      Jinmin Goh
# Date:        20200205
# URL: https://leetcode.com/problems/implement-trie-prefix-tree/

import sys

# set implementation
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


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)