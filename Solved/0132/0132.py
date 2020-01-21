# Problem No.: 132
# Solver:      Jinmin Goh
# Date:        20200121
# URL: https://leetcode.com/problems/palindrome-partitioning-ii/

import sys

class Solution:
    def minCut(self, s: str) -> int:
        # solve with DP
        if not s:
            return 0
        
        tempFlag = True
        for i in range(len(s) // 2):
            if s[i] != s[- i - 1]:
                tempFlag = False
        if tempFlag:
            return 0
        # holds s[:j + 1]'s minimum cut count
        ans = [i - 1 for i in range(len(s) + 1)]
        # holds whether s[j:i + 1] is palindrome
        dp_table = [[False] * (len(s) + 1) for i in range(len(s) + 1)]
        
        for i in range(1, len(s) + 1):
            for j in range(1, i + 1):
                if s[i - 1] == s[j - 1] and (i - j <= 2 or dp_table[j + 1][i - 1]):
                    dp_table[j][i] = True
                    if j == 1:
                        ans[i] = 0
                    else:
                        ans[i] = min(ans[i], ans[j - 1] + 1)
        return ans[-1]