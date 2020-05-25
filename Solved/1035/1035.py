# Problem No.: 1035
# Solver:      Jinmin Goh
# Date:        20200526
# URL: https://leetcode.com/problems/uncrossed-lines/

import sys

# LIS
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dpTable = [[0] * len(B) for _ in range(len(A))]
        for i in range(len(B)):
            if A[0] == B[i] or (i > 0 and dpTable[0][i - 1] == 1):
                dpTable[0][i] = 1
        for i in range(1, len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    if j == 0:
                        dpTable[i][j] = 1
                    else:
                        dpTable[i][j] = max(dpTable[i][j - 1], dpTable[i - 1][j - 1] + 1)
                else:
                    dpTable[i][j] = max(dpTable[i][j - 1], dpTable[i - 1][j])
        #print(dpTable)
        return dpTable[-1][-1]