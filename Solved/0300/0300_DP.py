# Problem No.: 300
# Solver:      Jinmin Goh
# Date:        20200217
# URL: https://leetcode.com/problems/longest-increasing-subsequence/

import sys

# DP solution, time: O(n^2) / space: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dpList = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dpList[i] = max(dpList[i], dpList[j] + 1)
        return max(dpList)