# Problem No.: 31
# Solver:      Jinmin Goh
# Date:        20191212
# URL: https://leetcode.com/problems/next-permutation/submissions/

import sys

class Solution(object):
    def nextPermutation(self, nums):
        if not nums:
            return
        p1 = len(nums) - 2
        # find first decreasing number from right
        while p1 >= 0 and nums[p1] >= nums[p1 + 1]:
            p1 -= 1
        if p1 < 0:
            nums.reverse()
            return
        minval = 2**31 - 1
        minval_pos = p1
        p2 = p1 + 1
        # find smallest and rightmost position for bigger than p1 position
        while p2 < len(nums):
            if minval >= nums[p2] and nums[p2] > nums[p1]:
                minval = nums[p2]
                minval_pos = p2
            p2 += 1
        
        # swap two values and reverse right part list
        temp = nums[minval_pos]
        nums[minval_pos] = nums[p1]
        nums[p1] = temp
        temp_list = nums[p1 + 1:]
        temp_list.reverse()
        for i in range(len(temp_list)):
            nums[p1 + 1 + i] = temp_list[i]
        return
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        