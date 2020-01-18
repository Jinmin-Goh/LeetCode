# Problem No.: 126
# Solver:      Jinmin Goh
# Date:        20200118
# URL: https://leetcode.com/problems/word-ladder-ii/

import sys


# good C++ solution: https://leetcode.com/problems/word-ladder-ii/discuss/40434/C%2B%2B-solution-using-standard-BFS-method-no-DFS-or-backtracking

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        ans = []
        pathList = [[beginWord]]
        wordList = set(wordList)
        visitedNode = set()
        length = 1
        minLength = 2 ** 31 - 1
        wordLen = len(beginWord)
        
        while pathList:
            path = pathList[0][:]
            pathList.pop(0)
            if len(path) > length:
                for i in visitedNode:
                    wordList.remove(i)
                visitedNode = set()
                if length > minLength:
                    break
                else:
                    length = len(path)
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            for i in range(wordLen):
                for j in alphabet:
                    tempstr = path[-1][:i] + j + path[-1][i + 1:]
                    if tempstr in wordList:
                        newPath = path + [tempstr]
                        visitedNode.add(tempstr)
                        if tempstr == endWord:
                            minLength = length
                            ans.append(newPath)
                        else:
                            pathList.append(newPath)
        return ans
                    
                