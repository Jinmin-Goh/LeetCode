# Problem No.: 55
# Solver:      Jinmin Goh
# Date:        20191221
# URL: https://leetcode.com/problems/jump-game/

import sys

class Solution(object):
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        p = 0
        while True:
            temp_p = p
            if nums[p] == 0:
                return False
            if nums[p] + p >= len(nums) - 1:
                return True
            temp_max = 0
            for i in range(nums[p]):
                if temp_max < nums[p + i + 1] + i + 1:
                    temp_max = nums[p + i + 1] + i + 1
                    temp_p = p + i + 1
            p = temp_p
            
        """
        :type nums: List[int]
        :rtype: bool
        """
        