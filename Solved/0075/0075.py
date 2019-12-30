# Problem No.: 75
# Solver:      Jinmin Goh
# Date:        20191230
# URL: https://leetcode.com/problems/sort-colors/

import sys

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if not nums:
            return nums
        cnt = [0,0,0]
        for i in nums:
            cnt[i] += 1
        temp = 0
        for i, val in enumerate(cnt):
            for j in range(val):
                nums[temp + j] = i
            temp += val
        """
        Do not return anything, modify nums in-place instead.
        """
        