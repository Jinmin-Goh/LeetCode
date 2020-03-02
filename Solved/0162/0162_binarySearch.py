# Problem No.: 162
# Solver:      Jinmin Goh
# Date:        20200302
# URL: https://leetcode.com/problems/find-peak-element/

import sys

# using binary search
# time: O(log n)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        pFront = 0
        pRear = len(nums) - 1
        pMid = (len(nums) - 1) // 2
        while pFront < pRear:
            pMid1 = (pFront + pRear) // 2
            pMid2 = pMid1 + 1
            #print(pFront, pMid1, pMid2, pRear)
            if (pFront == 0 or pMid1 == 0)and nums[0] > nums[1]:
                return 0
            if (pRear == len(nums) - 1 or pMid2 == len(nums) - 1) and nums[-2] < nums[-1]:
                return len(nums) - 1
            
            if nums[pFront - 1] < nums[pFront] and nums[pFront + 1] < nums[pFront]:
                return pFront
            if nums[pMid1 - 1] < nums[pMid1] and nums[pMid1 + 1] < nums[pMid1]:
                return pMid1
            if nums[pMid2 - 1] < nums[pMid2] and nums[pMid2 + 1] < nums[pMid2]:
                return pMid2
            if nums[pRear - 1] < nums[pRear] and nums[pRear + 1] < nums[pRear]:
                return pRear
            if nums[pMid1] < nums[pMid2]:
                pFront = pMid2
            else:
                pRear = pMid1
        return pFront