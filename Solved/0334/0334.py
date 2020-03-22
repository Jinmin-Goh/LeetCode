# Problem No.: 334
# Solver:      Jinmin Goh
# Date:        20200323
# URL: https://leetcode.com/problems/increasing-triplet-subsequence/

import sys

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        low = None
        mid = None
        for i in nums:
            if low == None:
                low = i
            elif i > low:
                if mid == None:
                    mid = i
                elif i > mid:
                    return True
                elif i < mid:
                    mid = i
            elif i < low:
                low = i
        return False