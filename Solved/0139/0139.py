# Problem No.: 139
# Solver:      Jinmin Goh
# Date:        20200124
# URL: https://leetcode.com/problems/word-break/

import sys

# DP solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordSet = set(wordDict)
        # memoization
        self.dp_list = [None] * len(s)
        return self.dp(s, wordDict)
    
    def dp(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict:
            return True
        flag = False
        for i in range(1, len(s)):
            if s[:i] in self.wordSet:
                if self.dp_list[i] == None:
                    self.dp_list[i] = flag or self.dp(s[i:], wordDict)
                flag = self.dp_list[i]
            if flag:
                break
        return flag        
            