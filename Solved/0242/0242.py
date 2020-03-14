# Problem No.: 242
# Solver:      Jinmin Goh
# Date:        20200314
# URL: https://leetcode.com/problems/valid-anagram/

import sys

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        for i in s:
            if i not in sDict:
                sDict[i] = 1
            else:
                sDict[i] += 1
        for i in t:
            if i not in sDict:
                return False
            else:
                sDict[i] -= 1
                if sDict[i] == 0:
                    del sDict[i]
        if sDict:
            return False
        return True