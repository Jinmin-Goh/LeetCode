# Problem No.: 53
# Solver:      Jinmin Goh
# Date:        20191221
# URL: https://leetcode.com/problems/maximum-subarray/

import sys

class Solution(object):
    def maxSubArray(self, nums):
        dp_table = []
        max_val = nums[0]
        for i in range(len(nums)):
            if not dp_table:
                dp_table.append(nums[i])
            else:
                dp_table.append(nums[i] + max(0, dp_table[i - 1]))
                max_val = max(max_val, dp_table[i])
        return max_val
        
        """
        :type nums: List[int]
        :rtype: int
        """
        