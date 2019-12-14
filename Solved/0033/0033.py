# Problem No.: 33
# Solver:      Jinmin Goh
# Date:        20191214
# URL: https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/

import sys

class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1
        pointer_front = 0
        pointer_rear = len(nums) - 1
        ans = 0
        # binary tree searching
        while pointer_front <= pointer_rear:
            pointer_mid = (pointer_rear + pointer_front) // 2 
            if nums[pointer_front] == target:
                return pointer_front
            if nums[pointer_rear] == target:
                return pointer_rear
            if nums[pointer_mid] == target:
                return pointer_mid
            
            # left half ascending
            if nums[pointer_front] < nums[pointer_mid]:
                if nums[pointer_front] < target < nums[pointer_mid]:
                    pointer_rear = pointer_mid - 1
                else:
                    pointer_front = pointer_mid + 1
            # right half ascending
            else:
                if nums[pointer_mid] < target < nums[pointer_rear]:
                    pointer_front = pointer_mid + 1
                else:
                    pointer_rear = pointer_mid - 1
        return -1
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        