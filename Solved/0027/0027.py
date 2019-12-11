# Problem No.: 27
# Solver:      Jinmin Goh
# Date:        20191211
# URL: https://leetcode.com/problems/remove-element/submissions/

import sys

class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        if val not in nums:
            return len(nums)
        pointer_front = 0
        pointer_rear = len(nums) - 1
        cnt = 0
        while pointer_front < pointer_rear:
            while nums[pointer_front] != val:
                pointer_front += 1
                cnt += 1
            while pointer_rear >= 0 and nums[pointer_rear] == val:
                pointer_rear -= 1
            if pointer_front >= pointer_rear:
                break
            nums[pointer_front] = nums[pointer_rear]
            nums[pointer_rear] = val
        return cnt
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        