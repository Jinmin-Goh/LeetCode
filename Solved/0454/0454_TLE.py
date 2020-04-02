# Problem No.: 454
# Solver:      Jinmin Goh
# Date:        20200402
# URL: https://leetcode.com/problems/4sum-ii/

# 46/48 passed and TLE
# time: O(n^4) when list length is n

import sys

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        abDict = {}
        abcDict = {}
        
        cdDict = {}
        ans = 0
        for i in A:
            for j in B:
                if i + j not in abDict:
                    abDict[i + j] = 1
                else:
                    abDict[i + j] += 1
        for i in C:
            for j in D:
                if i + j not in cdDict:
                    cdDict[i + j] = 1
                else:
                    cdDict[i + j] += 1
        for i in abDict:
            for j in cdDict:
                if i + j == 0:
                    ans += abDict[i] * cdDict[j]
        return ans