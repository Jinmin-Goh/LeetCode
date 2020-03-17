# Problem No.: 315
# Solver:      Jinmin Goh
# Date:        20200317
# URL: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

# 15/16 passed and TLE
# time: O(n^2)

import sys

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        ans = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    ans[i] += 1
        return ans