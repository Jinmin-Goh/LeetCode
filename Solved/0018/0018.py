# Problem No.: 18
# Solver:      Jinmin Goh
# Date:        20191208
# URL: https://leetcode.com/problems/4sum/submissions/

import sys

class Solution(object):
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        nums.sort()
        ans = []
        ans_set = set()
        pointer_hold_1 = 0
        pointer_hold_2 = pointer_hold_1 + 1
        pointer_front = pointer_hold_2 + 1
        pointer_rear = len(nums) - 1
        while pointer_hold_1 < len(nums) - 3:
            while pointer_hold_2 < len(nums) - 2:
                while pointer_front < pointer_rear:
                    if nums[pointer_hold_1] + nums[pointer_hold_2] + nums[pointer_front] + nums[pointer_rear] > target:
                        pointer_rear -= 1
                    elif nums[pointer_hold_1] + nums[pointer_hold_2] + nums[pointer_front] + nums[pointer_rear] < target:
                        pointer_front += 1
                    elif tuple([nums[pointer_hold_1], nums[pointer_hold_2], nums[pointer_front], nums[pointer_rear]]) not in ans_set:
                        ans_set.add(tuple([nums[pointer_hold_1], nums[pointer_hold_2], nums[pointer_front], nums[pointer_rear]]))
                        ans.append([nums[pointer_hold_1], nums[pointer_hold_2], nums[pointer_front], nums[pointer_rear]])
                        pointer_front += 1
                    else:
                        pointer_front += 1
                pointer_hold_2 += 1
                pointer_front = pointer_hold_2 + 1
                pointer_rear = len(nums) - 1
            
            pointer_hold_1 += 1
            pointer_hold_2 = pointer_hold_1 + 1
            pointer_front = pointer_hold_2 + 1
            pointer_rear = len(nums) - 1
        return ans
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        