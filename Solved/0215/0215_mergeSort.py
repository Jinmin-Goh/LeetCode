# Problem No.: 215
# Solver:      Jinmin Goh
# Date:        20200206
# URL: https://leetcode.com/problems/kth-largest-element-in-an-array/

import sys

# time: O(n log n) / memory: O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = self.mergeSort(nums) # also able to use defalut sort function
        return nums[-k]
    
    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        else:
            left = self.mergeSort(nums[:len(nums) // 2])
            right = self.mergeSort(nums[len(nums) // 2:])
            temp = []
            while left and right:
                if left[0] > right[0]:
                    temp.append(right.pop(0))
                else:
                    temp.append(left.pop(0))
            if left:
                temp += left
            if right:
                temp += right
            return temp