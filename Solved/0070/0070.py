# Problem No.: 70
# Solver:      Jinmin Goh
# Date:        20191228
# URL: https://leetcode.com/problems/climbing-stairs/

import sys

class Solution:
    def climbStairs(self, n: int) -> int:
        self.dp = {1:1, 2:2}
        ans = self.dpProcess(n)
        return ans
    def dpProcess(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            if not self.dp.get(n-1):
                self.dp[n-1] = self.climbStairs(n-1)
            if not self.dp.get(n-2):
                self.dp[n-2] = self.climbStairs(n-2)
            return self.dp[n-1] + self.dp[n-2]
        