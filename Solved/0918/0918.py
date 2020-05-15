# Problem No.: 918
# Solver:      Jinmin Goh
# Date:        20200516
# URL: https://leetcode.com/problems/maximum-sum-circular-subarray/

import sys

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if not A:
            return 0
        totalSum = sum(A)
        curMax = A[0]
        curSumMax = A[0]
        curMin = A[0]
        curSumMin = A[0]
        
        for i in range(1, len(A)):
            curMax = max(A[i], curMax + A[i])
            curSumMax = max(curSumMax, curMax)
            curMin = min(A[i], curMin + A[i])
            curSumMin = min(curSumMin, curMin)
        if curSumMax < 0:
            return curSumMax
        ans = max(curSumMax, totalSum - curSumMin)
        return ans
                    