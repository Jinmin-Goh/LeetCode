# Problem No.: 41
# Solver:      Jinmin Goh
# Date:        20191216
# URL: https://leetcode.com/problems/first-missing-positive/

import sys

class Solution(object):
    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        
        check_list = [False] * len(nums)
        for i in range(len(nums)):
            if 0 < nums[i] <= len(nums):
                check_list[nums[i] - 1] = True
        i = 0
        while i < len(check_list) and check_list[i]:
            i += 1
        return i + 1
        """
        :type nums: List[int]
        :rtype: int
        """
        