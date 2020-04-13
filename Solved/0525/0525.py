# Problem No.: 525
# Solver:      Jinmin Goh
# Date:        20200414
# URL: https://leetcode.com/problems/contiguous-array/

import sys

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        temp = 0
        sumDict = {}
        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
            else:
                temp -= 1
            if temp in sumDict:
                sumDict[temp].append(i)
            else:
                sumDict[temp] = [i]
        ans = 0
        for i in sumDict:
            if i == 0:
                ans = max(ans, max(sumDict[i]) + 1)
            else:
                ans = max(ans, max(sumDict[i]) - min(sumDict[i]))
        return ans