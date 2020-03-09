# Problem No.: 217
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://leetcode.com/problems/contains-duplicate/

import sys

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for i in nums:
            if i not in numSet:
                numSet.add(i)
            else:
                return True
        return False
            