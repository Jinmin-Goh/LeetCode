# Problem No.: 154
# Solver:      Jinmin Goh
# Date:        20200726
# URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

import sys

# O(n), short answer

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)