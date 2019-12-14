# Problem No.: 35
# Solver:      Jinmin Goh
# Date:        20191214
# URL: https://leetcode.com/problems/search-insert-position/submissions/

import sys

class Solution(object):
    def searchInsert(self, nums, target):
        if not nums:
            return 0
        p_front = 0
        p_rear = len(nums) - 1
        while p_front <= p_rear:
            p_mid = (p_front + p_rear) // 2
            if nums[p_front] >= target:
                return p_front
            if nums[p_rear] < target:
                return p_rear + 1
            if nums[p_mid] >= target:
                p_rear = p_mid - 1
            else:
                p_front = p_mid + 1
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        