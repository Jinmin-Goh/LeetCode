# Problem No.: 1
# Solver:      Jinmin Goh
# Date:        20191201
# URL: https://leetcode.com/problems/two-sum/

import sys

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        