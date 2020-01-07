# Problem No.: 97
# Solver:      Jinmin Goh
# Date:        20200107
# URL: https://leetcode.com/problems/interleaving-string/

import sys

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if not s3:
            if s1 or s2:
                return False
            else: 
                return True
        if not s1:
            if s2 == s3:
                return True
            else:
                return False
        if not s2:
            if s1 == s3:
                return True
            else:
                return False
        
        # DP solution
        self.dp_table = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        self.dp_table[0][0] = True
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        
        self.dp(0, 0)
        print()
        return self.dp_table[len(s1)][len(s2)]
       
        
    def dp(self, i: int, j: int) -> None:
        #print(i, j)
        if i < len(self.s1) and self.s1[i] == self.s3[i + j] and not self.dp_table[i + 1][j]:
            self.dp_table[i + 1][j] = True
            self.dp(i + 1, j)
        if j < len(self.s2) and self.s2[j] == self.s3[i + j] and not self.dp_table[i][j + 1]:
            self.dp_table[i][j + 1] = True
            self.dp(i, j + 1)