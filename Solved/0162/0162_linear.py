# Problem No.: 162
# Solver:      Jinmin Goh
# Date:        20200302
# URL: https://leetcode.com/problems/find-peak-element/

import sys

# linear search
# time: O(n)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            if i == 0 and nums[0] > nums[1]:
                return i
            if i == len(nums) - 1 and nums[-2] < nums[-1]:
                return i
            if 0 < i < len(nums) - 1 and nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
                return i