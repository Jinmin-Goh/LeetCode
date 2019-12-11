# Problem No.: 26
# Solver:      Jinmin Goh
# Date:        20191211
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/

import sys

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        temp = list(set(nums))
        temp.sort()
        for i in range(len(temp)):
            nums[i] = temp[i]
        return len(temp)
        """
        :type nums: List[int]
        :rtype: int
        """
        