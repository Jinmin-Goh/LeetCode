# Problem No.: 140
# Solver:      Jinmin Goh
# Date:        20200126
# URL: https://leetcode.com/problems/word-break-ii/

import sys

# 31/39 passed and TLE solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s or not wordDict:
            return []
        self.wordSet = set(wordDict)
        self.len = len(s)
        self.ans = []
        self.dp(s, "")
        return self.ans
    
    def dp(self, s: str, tempList = str) -> None:
        if s in self.wordSet:
            if not tempList:
                tempAns = s
            else:
                tempAns = tempList + " " + s
            self.ans.append(tempAns)
        for i in range(1, len(s)):
            if s[:i] in self.wordSet:
                if not tempList:
                    tempAns = s[:i]
                else:
                    tempAns = tempList + " "+ s[:i]
                #self.dp_list[self.len - len(s) + i - 1].append(tempAns)
                self.dp(s[i:], tempAns)