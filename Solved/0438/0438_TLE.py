# Problem No.: 438
# Solver:      Jinmin Goh
# Date:        20200225
# URL: https://leetcode.com/problems/find-all-anagrams-in-a-string/

import sys

# 35/36 passed and TLE

import copy
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        ans = []
        pDict = {}
        for i in p:
            if i not in pDict:
                pDict[i] = 1
            else:
                pDict[i] += 1
        for i in range(len(s) - len(p) + 1):
            if s[i] in pDict:
                tempDict = copy.deepcopy(pDict)
                flag = True
                #print(temp, tempDict)
                for j in range(i, i + len(p)):
                    if s[j] not in tempDict or tempDict[s[j]] == 0:
                        flag = False
                        break
                    tempDict[s[j]] -= 1
                if flag:
                    ans.append(i)
        return ans