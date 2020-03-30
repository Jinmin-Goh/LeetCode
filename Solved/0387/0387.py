# Problem No.: 387
# Solver:      Jinmin Goh
# Date:        20200330
# URL: https://leetcode.com/problems/first-unique-character-in-a-string/

import sys

class Solution:
    def firstUniqChar(self, s: str) -> int:
        wordDict = {}
        for i in range(len(s)):
            if s[i] not in wordDict:
                wordDict[s[i]] = [i,1]
            else:
                wordDict[s[i]][1] += 1
        for i in wordDict:
            if wordDict[i][1] == 1:
                return wordDict[i][0]
        return -1