# Problem No.: 1143
# Solver:      Jinmin Goh
# Date:        20200427
# URL: https://leetcode.com/problems/longest-common-subsequence/

import sys

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        
        dpTable = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dpTable[i][j] = dpTable[i - 1][j - 1] + 1
                else:
                    dpTable[i][j] = max(dpTable[i][j - 1], dpTable[i - 1][j])
        #print(dpTable)
        return dpTable[-1][-1]
                