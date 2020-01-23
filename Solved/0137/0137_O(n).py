# Problem No.: 137
# Solver:      Jinmin Goh
# Date:        20200123
# URL: https://leetcode.com/problems/single-number-ii/

import sys

# time: O(n) / space: O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ansDict = {}
        for i in nums:
            if i not in ansDict:
                ansDict[i] = 1
            else:
                ansDict[i] += 1
        for i in ansDict:
            if ansDict[i] == 1:
                return i