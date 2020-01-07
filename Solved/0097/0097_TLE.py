# Problem No.: 97
# Solver:      Jinmin Goh
# Date:        20200107
# URL: https://leetcode.com/problems/interleaving-string/

import sys

# 89/101 passed TLE solution
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
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
            
        if s1[0] != s3[0] and s2[0] != s3[0]:
            return False
        flag1 = False
        flag2 = False
        if s1[0] == s3[0]:
            flag1 = self.isInterleave(s1[1:], s2, s3[1:])
        if s2[0] == s3[0]:
            flag2 = self.isInterleave(s1, s2[1:], s3[1:])
        return flag1 or flag2