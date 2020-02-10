# Problem No.: 238
# Solver:      Jinmin Goh
# Date:        20200210
# URL: https://leetcode.com/problems/product-of-array-except-self/

import sys

# time: O(n) / space: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        temp = 1
        for i in range(len(nums) - 1):
            temp *= nums[i]
            ans.append(temp)
        temp = 1
        for i in reversed(range(1, len(nums))):
            temp *= nums[i]
            ans[i - 1] *= temp
        return ans