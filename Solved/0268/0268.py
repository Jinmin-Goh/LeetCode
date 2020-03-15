# Problem No.: 268
# Solver:      Jinmin Goh
# Date:        20200315
# URL: https://leetcode.com/problems/missing-number/

import sys

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mask = 1
        for i in range(len(nums)):
            mask = mask << 1 | 1
        #print(mask)
        for i in nums:
            mask ^= 2 ** i
        ans = 0
        while mask % 2 == 0:
            mask >>= 1
            ans += 1
        return ans
        