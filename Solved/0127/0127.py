# Problem No.: 127
# Solver:      Jinmin Goh
# Date:        20200118
# URL: https://leetcode.com/problems/word-ladder/

import sys

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList = set(wordList)
        wordLength = len(beginWord)
        length = 1
        visitedNode = [beginWord]
        alphabet = "abcdefghijklmnopqrstuvwxyz"
            
        while visitedNode:
            tempList = []
            for i in visitedNode:
                if i in wordList:
                    wordList.remove(i)
            for i in visitedNode:
                for j in range(wordLength):
                    for k in alphabet:
                        tempstr = i[:j] + k + i[j + 1:]
                        if tempstr in wordList:
                            tempList.append(tempstr)
                            if tempstr == endWord:
                                return length + 1
            length += 1
            visitedNode = tempList[:]
        return 0