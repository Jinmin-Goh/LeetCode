# Problem No.: 16
# Solver:      Jinmin Goh
# Date:        20191208
# URL: https://leetcode.com/problems/3sum-closest/

import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        min_diff = 2 ** 31 - 1
        ans = 0
        pointer_hold = 0
        pointer_front = pointer_hold + 1
        pointer_rear = len(nums) - 1
        while pointer_hold < len(nums) - 2:
            while pointer_front < pointer_rear:
                #print("before:",min_diff, ans, pointer_hold, pointer_front, pointer_rear)
                # if same
                if nums[pointer_hold] + nums[pointer_front] + nums[pointer_rear] == target:
                    return target
                # if found more closer answer
                if abs(nums[pointer_hold] + nums[pointer_front] + nums[pointer_rear] - target) < min_diff:
                    min_diff = abs(nums[pointer_hold] + nums[pointer_front] + nums[pointer_rear] - target)
                    ans = nums[pointer_hold] + nums[pointer_front] + nums[pointer_rear]
                    
                # if searching is bigger than target
                if nums[pointer_hold] + nums[pointer_front] + nums[pointer_rear] > target:
                    pointer_rear -= 1
                # if searching is smaller than target
                elif nums[pointer_hold] + nums[pointer_front] + nums[pointer_rear] < target:
                    pointer_front += 1
                #print("after:",min_diff, ans, pointer_hold, pointer_front, pointer_rear)
            pointer_hold += 1
            pointer_front = pointer_hold + 1
            pointer_rear = len(nums) - 1
        return ans
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        