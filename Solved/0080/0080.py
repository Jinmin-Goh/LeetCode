# Problem No.: 80
# Solver:      Jinmin Goh
# Date:        20191231
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

import sys

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return
        p_front = 0
        p_rear = len(nums) - 1
        temp_num = None
        duplFlag = False
        while p_front <= p_rear:
            if temp_num == None:
                temp_num = nums[0]
            elif temp_num == nums[p_front] and not duplFlag:
                duplFlag = True
            elif temp_num == nums[p_front] and duplFlag:
                for i in range(p_front, p_rear):
                    nums[i] = nums[i + 1]
                p_rear -= 1
                continue
            elif temp_num != nums[p_front]:
                temp_num = nums[p_front]
                duplFlag = False
            p_front += 1
        return p_rear + 1