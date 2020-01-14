# Problem No.: 115
# Solver:      Jinmin Goh
# Date:        20200114
# URL: https://leetcode.com/problems/distinct-subsequences/

import sys


# solution link: https://leetcode.com/problems/distinct-subsequences/discuss/37327/Easy-to-understand-DP-in-Java
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dpTable = [[0] * (len(s) + 1) for i in range(len(t) + 1)]
        for i in range(len(s) + 1):
            dpTable[0][i] = 1
        for i in range(1,len(t) + 1):
            for j in range(1, len(s) + 1):
                if t[i - 1] == s[j - 1]:
                    dpTable[i][j] = dpTable[i - 1][j - 1] + dpTable[i][j - 1]
                else:
                    dpTable[i][j] = dpTable[i][j - 1]
        return dpTable[len(t)][len(s)]