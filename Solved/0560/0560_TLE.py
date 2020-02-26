# Problem No.: 560
# Solver:      Jinmin Goh
# Date:        20200226
# URL: https://leetcode.com/problems/subarray-sum-equals-k/

import sys

# 69/80 passed and TLE
# time: O(n^2)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        pFront = 0
        pRear = 0
        ans = 0
        sumList = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            sumList[i] = sumList[i - 1] + nums[i - 1]
        for i in range(len(sumList) - 1):
            for j in range(i + 1, len(sumList)):
                if sumList[j] - sumList[i] == k:
                    ans += 1
        return ans