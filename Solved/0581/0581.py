# Problem No.: 581
# Solver:      Jinmin Goh
# Date:        20200227
# URL: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

import sys

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        i = 1
        while i < len(nums) and nums[i - 1] <= nums[i]:
            i += 1
        pFront = i - 1
        i = len(nums) - 1
        while i > 0 and nums[i - 1] <= nums[i]:
            i -= 1
        pRear = i
        if pFront > pRear:
            return 0
        midMin = min(nums[pFront:pRear + 1])
        midMax = max(nums[pFront:pRear + 1])
        ans = pRear - pFront + 1
        i = pFront - 1
        while i >= 0 and nums[i] > midMin:
            ans += 1
            i -= 1
        i = pRear + 1
        while i < len(nums) and nums[i] < midMax:
            ans += 1
            i += 1
        return ans