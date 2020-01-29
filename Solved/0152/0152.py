# Problem No.: 152
# Solver:      Jinmin Goh
# Date:        20200129
# URL: https://leetcode.com/problems/maximum-product-subarray/

import sys

# time: O(n) / memory: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxVal = nums[0]
        minVal = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxVal, minVal = minVal, maxVal
            maxVal = max(nums[i], nums[i] * maxVal)
            minVal = min(nums[i], nums[i] * minVal)
            ans = max(ans, maxVal)
        return ans