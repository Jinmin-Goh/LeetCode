# Problem No.: 448
# Solver:      Jinmin Goh
# Date:        20200225
# URL: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

import sys

# time: O(n^2) / space: O(1)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return 
        bit = 0
        for i in nums:
            temp = 1 << i - 1
            bit |= temp
        ans = []
        for i in range(len(nums)):
            if not bit % 2:
                ans.append(i + 1)
            bit >>= 1
        return ans
