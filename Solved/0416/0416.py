# Problem No.: 416
# Solver:      Jinmin Goh
# Date:        20200224
# URL: https://leetcode.com/problems/partition-equal-subset-sum/

import sys

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        nums.sort()
        sumVal = sum(nums)
        if sumVal % 2:
            return False
        target = sumVal // 2
        if nums[-1] > target:
            return False
        if nums[-1] == target:
            return True
        # if list is valid, all of elements should be coutained in one of two lists
        if nums[0] > target - nums[-1]:
            return False
        return self.find(nums[:-1], target - nums[-1])
        
    def find(self, nums: List[int], target: int) -> bool:
        ans = False
        if nums[0] > target:
            return False
        if target in nums:
            return True
        for i in range(len(nums)):
            if ans:
                break
            #print("test")
            temp = nums[:]
            val = temp.pop(i)
            tempBool = self.find(temp, target - val)
            ans = ans or tempBool
        return ans