# Problem No.: 136
# Solver:      Jinmin Goh
# Date:        20200123
# URL: https://leetcode.com/problems/single-number/

import sys

# using hash set for checking
# time: O(n) / space: O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        numSet = set()
        for i in nums:
            if i in numSet:
                numSet.remove(i)
            else:
                numSet.add(i)
        return list(numSet)[0]