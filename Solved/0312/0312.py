# Problem No.: 312
# Solver:      Jinmin Goh
# Date:        20200219
# URL: https://leetcode.com/problems/burst-balloons/

import sys

# good solution link 1: https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations
# good solution link 2: https://leetcode.com/problems/burst-balloons/discuss/76229/For-anyone-that-is-still-confused-after-reading-all-kinds-of-explanations...
# O(n^3) solution

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # remove 0 first
        numsNonZero = [1]
        for i in nums:
            if i != 0:
                numsNonZero.append(i)
        numsNonZero.append(1)
        n = len(numsNonZero)
        
        if n == 2:
            return 0
        
        dp = [[0] * n for i in range(n)]
        
        for i in range(2, n):
            for left in range(0, n - i):
                right = left + i
                for j in range(left + 1,right):
                    dp[left][right] = max(dp[left][right], numsNonZero[left] * numsNonZero[j] * numsNonZero[right] + dp[left][j] + dp[j][right])
        return dp[0][n - 1]