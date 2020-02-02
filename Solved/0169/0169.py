# Problem No.: 169
# Solver:      Jinmin Goh
# Date:        20200202
# URL: https://leetcode.com/problems/majority-element/

import sys

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        countDict = {}
        for i in nums:
            if i not in countDict:
                countDict[i] = 1
            else:
                countDict[i] += 1
            if countDict[i] > length // 2:
                return i
                