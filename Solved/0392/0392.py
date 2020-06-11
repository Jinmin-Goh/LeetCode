# Problem No.: 392
# Solver:      Jinmin Goh
# Date:        20200610
# URL: https://leetcode.com/problems/is-subsequence/

import sys

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        flag = False
        pointer = 0
        for i in t:
            #print(i, s[pointer])
            if i == s[pointer]:
                pointer += 1
            
            if pointer == len(s):
                flag = True
                break
        return flag