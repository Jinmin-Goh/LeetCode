# Problem No.: 287
# Solver:      Jinmin Goh
# Date:        20200213
# URL: https://leetcode.com/problems/find-the-duplicate-number/

import sys

# 52/53 passed and TLE
# O(n^2) solution
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        frontP = 0
        rearP = len(nums) - 1
        while True:
            temp = nums[frontP]
            for i in range(frontP + 1, rearP + 1):
                if nums[i] == temp:
                    return temp
            frontP += 1
            temp = nums[rearP]
            for i in reversed(range(frontP, rearP)):
                if nums[i] == temp:
                    return temp
            rearP -= 1