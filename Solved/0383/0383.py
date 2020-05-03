# Problem No.: 383
# Solver:      Jinmin Goh
# Date:        20200503
# URL: https://leetcode.com/problems/ransom-note/

import sys

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magDict = {}
        for i in magazine:
            if i not in magDict:
                magDict[i] = 1
            else:
                magDict[i] += 1
        noteDict = {}
        for i in ransomNote:
            if i not in noteDict:
                noteDict[i] = 1
            else:
                noteDict[i] += 1
        for i in noteDict:
            if i not in magDict or noteDict[i] > magDict[i]:
                return False
        return True