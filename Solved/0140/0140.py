# Problem No.: 140
# Solver:      Jinmin Goh
# Date:        20200126
# URL: https://leetcode.com/problems/word-break-ii/

import sys

# DP memoization
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordSet = set(wordDict)
        self.len = len(s)
        # memoization
        self.dp_dict = {}
        return self.dp(s, wordDict)

    
    def dp(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return []
        if s in self.dp_dict:
            return self.dp_dict[s]
        
        temp = []
        for word in wordDict:
            if len(s) < len(word):
                continue
            if word == s:
                temp.append(word)
            elif word == s[:len(word)]:
                tempAns = self.dp(s[len(word):], wordDict)
                for tempWord in tempAns:
                    temp.append(word + " " + tempWord)
        self.dp_dict[s] = temp
        return temp