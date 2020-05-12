# Problem No.: 540
# Solver:      Jinmin Goh
# Date:        20200512
# URL: https://leetcode.com/problems/single-element-in-a-sorted-array/

import sys

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        pFront = 0
        pRear = len(nums) - 1
        while pFront < pRear:
            pMid = (pFront + pRear) // 2
            if pMid % 2:
                if nums[pMid] != nums[pMid - 1]:
                    pRear = pMid - 1
                else:
                    pFront = pMid + 1
            else:
                if nums[pMid] != nums[pMid + 1]:
                    pRear = pMid
                else:
                    pFront = pMid + 2
        return nums[pRear]