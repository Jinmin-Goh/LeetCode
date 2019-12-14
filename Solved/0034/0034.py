# Problem No.: 34
# Solver:      Jinmin Goh
# Date:        20191214
# URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/

import sys

class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1,-1]
        p_front = 0
        p_rear = len(nums) - 1
        p_target = 0
        ans = []
        # find target first
        while p_front <= p_rear:
            p_mid = (p_front + p_rear) // 2
            if nums[p_front] == target:
                p_target = p_front
                break
            if nums[p_rear] == target:
                p_target = p_rear
                break
            if nums[p_mid] == target:
                p_target = p_mid
                break
            if nums[p_mid] < target:
                p_front = p_mid + 1
            else:
                p_rear = p_mid - 1
        if p_front > p_rear:
            return [-1,-1]
        # find first non-target from left
        p_front = 0
        p_rear = p_target
        while p_front <= p_rear:
            p_mid = (p_front + p_rear) // 2
            if nums[p_front] == target:
                ans.append(p_front)
                break
            if nums[p_rear] != target:
                ans.append(p_rear + 1)
                break
            if nums[p_mid] == target:
                p_rear = p_mid - 1
            else:
                p_front = p_mid + 1
        # find last target from right
        p_front = p_target
        p_rear = len(nums) - 1
        while p_front <= p_rear:
            p_mid = (p_front + p_rear) // 2
            if nums[p_front] != target:
                ans.append(p_front - 1)
                break
            if nums[p_rear] == target:
                ans.append(p_rear)
                break
            if nums[p_mid] == target:
                p_front = p_mid + 1
            else:
                p_rear = p_mid - 1
        return ans

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        