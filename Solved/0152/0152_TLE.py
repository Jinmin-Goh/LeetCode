# Problem No.: 152
# Solver:      Jinmin Goh
# Date:        20200129
# URL: https://leetcode.com/problems/maximum-product-subarray/

import sys

# 183/184 accepted and TLE
# time: O(n^2) / memory: O(n)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_list = [None] * len(nums)
        ans = nums[0]
        dp_list[0] = nums[0]
        for i in range(1, len(nums)):
            temp = [None] * len(nums)
            for j in range(i + 1):
                #print(i, j, dp_list, temp)
                if i == j:
                    temp[j] = nums[j]
                else:
                    temp[j] = nums[i] * dp_list[j]
                ans = max(ans, temp[j])
            dp_list = temp[:]
        return ans
                
                