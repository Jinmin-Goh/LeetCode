# Problem No.: 179
# Solver:      Jinmin Goh
# Date:        20200304
# URL: https://leetcode.com/problems/largest-number/

import sys

# Bubble sort
# time: O(n^2)

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
        zeroFlag = True
        for i in nums:
            if i != 0:
                zeroFlag = False
                break
        if zeroFlag:
            return "0"
        for i in range(1, len(nums)):
            for j in reversed(range(i, len(nums))):
                if int(str(nums[j]) + str(nums[j - 1])) > int(str(nums[j - 1]) + str(nums[j])):
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
        print(nums)
        ans = ""
        for i in nums:
            ans += str(i)
        return ans