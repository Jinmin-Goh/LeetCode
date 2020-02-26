# Problem No.: 560
# Solver:      Jinmin Goh
# Date:        20200226
# URL: https://leetcode.com/problems/subarray-sum-equals-k/

import sys

# used hash table
# time: O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pFront = 0
        pRear = 0
        ans = 0
        sumDict = {0:1}
        sumVal = 0
        for i in nums:
            sumVal += i
            if sumVal - k in sumDict:
                ans += sumDict[sumVal - k]
            if sumVal not in sumDict:
                sumDict[sumVal] = 1
            else:
                sumDict[sumVal] += 1
        return ans