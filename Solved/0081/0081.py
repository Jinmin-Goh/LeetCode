# Problem No.: 81
# Solver:      Jinmin Goh
# Date:        20191231
# URL: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

import sys

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        i = 0
        while i < len(nums) - 1:
            if nums[i] > nums[i + 1]:
                break
            i += 1
        rev_pos = i
        p_front = 0
        p_mid = len(nums) // 2
        p_rear = len(nums) - 1
        while p_front <= p_mid <= p_rear:
            #print(p_front, p_mid, p_rear)
            if nums[p_front] == target or nums[p_mid] == target or nums[p_rear] == target:
                return True
            if p_mid <= rev_pos:
                if nums[p_front] < target < nums[p_mid]:
                    p_rear = p_mid - 1
                    p_mid = (p_front + p_rear) // 2
                else:
                    p_front = p_mid + 1
                    p_mid = (p_front + p_rear) // 2
            else:
                if nums[p_mid] < target < nums[p_rear]:
                    p_front = p_mid + 1
                    p_mid = (p_front + p_rear) // 2
                else:
                    p_rear = p_mid - 1
                    p_mid = (p_front + p_rear) // 2
        return False