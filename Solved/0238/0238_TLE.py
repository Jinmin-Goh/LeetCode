# Problem No.: 238
# Solver:      Jinmin Goh
# Date:        20200210
# URL: https://leetcode.com/problems/product-of-array-except-self/

import sys

# 16/17 passed and TLE
# time: O(n^2) / space: O(1)
# needs no division and O(n) time complexity
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            temp = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                temp *= nums[j]
            ans.append(temp)
        return ans