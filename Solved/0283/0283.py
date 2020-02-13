# Problem No.: 283
# Solver:      Jinmin Goh
# Date:        20200213
# URL: https://leetcode.com/problems/move-zeroes/

import sys

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[cnt] = nums[cnt], nums[i]
                cnt += 1