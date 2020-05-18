# Problem No.: 567
# Solver:      Jinmin Goh
# Date:        20200519
# URL: https://leetcode.com/problems/permutation-in-string/

import sys

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        sDict = {}
        for i in s1:
            if i not in sDict:
                sDict[i] = 1
            else:
                sDict[i] += 1
        for i in range(len(s1)):
            if s2[i] in sDict:
                sDict[s2[i]] -= 1
        flag = True
        for i in sDict:
            if sDict[i]:
                flag = False
                break
        if flag:
            return True
        for i in range(len(s1), len(s2)):
            if s2[i - len(s1)] in sDict:
                sDict[s2[i - len(s1)]] += 1
            if s2[i] in sDict:
                sDict[s2[i]] -= 1
            flag = True
            for i in sDict:
                if sDict[i] != 0:
                    flag = False
                    break
            if flag:
                return True
        return False