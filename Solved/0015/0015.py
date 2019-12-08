# Problem No.: 15
# Solver:      Jinmin Goh
# Date:        20191207
# URL: 

import sys

class Solution(object):
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        ans_list = []
        ans_set = set()
        pointer_hold = 0
        pointer_front = pointer_hold + 1
        pointer_rear = len(nums) - 1
        while nums[pointer_hold] <= 0 and pointer_hold < len(nums) - 2:
            while pointer_front < pointer_rear:
                if nums[pointer_front] + nums[pointer_rear] + nums[pointer_hold] > 0:
                    pointer_rear -= 1
                elif nums[pointer_front] + nums[pointer_rear] + nums[pointer_hold] < 0:
                    pointer_front += 1
                elif not(tuple([nums[pointer_hold],nums[pointer_front],nums[pointer_rear]]) in ans_set):
                    ans_set.add(tuple([nums[pointer_hold],nums[pointer_front],nums[pointer_rear]]))
                    ans_list.append([nums[pointer_hold],nums[pointer_front],nums[pointer_rear]])
                    pointer_front += 1
                else:
                    pointer_front += 1
            pointer_hold += 1
            pointer_front = pointer_hold + 1
            pointer_rear = len(nums) - 1
            
        return ans_list
        
        """
        nums.sort()
        ans_list = []
        pointer_front = 0
        pointer_rear = len(nums) - 1
        while pointer_rear - pointer_front >= 2 and nums[pointer_rear] >= 0:
            while nums[pointer_front] <= 0 and pointer_rear - pointer_front >= 2:
                if nums[pointer_front + 1:pointer_rear].count(-(nums[pointer_front] + nums[pointer_rear])) > 0:
                    if not(list([nums[pointer_front],-(nums[pointer_front] + nums[pointer_rear]),nums[pointer_rear]]) in ans_list):
                        ans_list.append([nums[pointer_front],-(nums[pointer_front] + nums[pointer_rear]),nums[pointer_rear]])
                pointer_front += 1
            pointer_rear -= 1
            pointer_front = 0
        return ans_list
        """
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        