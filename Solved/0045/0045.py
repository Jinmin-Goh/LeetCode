# Problem No.: 45
# Solver:      Jinmin Goh
# Date:        20191219
# URL: https://leetcode.com/problems/jump-game-ii/

import sys

class Solution(object):
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        p = 0
        cnt = 0
        while p < len(nums):
            if nums[p] + p >= len(nums) - 1:
                return cnt + 1
            temp_max = 0
            temp_p = 0
            if nums[p] == 1:
                p += 1
                cnt += 1
            else:
                for i in range(1,nums[p] + 1):
                    if temp_max < p + i + nums[p + i]:
                        temp_max = p + i + nums[p + i]
                        temp_p = p + i
                p = temp_p
                cnt += 1
        """
        :type nums: List[int]
        :rtype: int
        """
        