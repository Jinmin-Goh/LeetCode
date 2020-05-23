# Problem No.: 451
# Solver:      Jinmin Goh
# Date:        20200523
# URL: https://leetcode.com/problems/sort-characters-by-frequency/

import sys

class Solution:
    def frequencySort(self, s: str) -> str:
        wordDict = {}
        for i in s:
            if i not in wordDict:
                wordDict[i] = 1
            else:
                wordDict[i] += 1
        temp = list(wordDict.items())
        pairList = []
        for i in temp:
            pairList.append((i[1], i[0]))
        pairList.sort()
        pairList = list(reversed(pairList))
        ans = ""
        for i in pairList:
            ans += i[0] * i[1]
        return ans