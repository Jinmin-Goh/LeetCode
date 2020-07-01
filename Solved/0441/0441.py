# Problem No.: 441
# Solver:      Jinmin Goh
# Date:        20200701
# URL: https://leetcode.com/problems/arranging-coins/

import sys

class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        cnt = 1
        while n >= cnt:
            ans += 1
            n -= cnt
            cnt += 1
        
        return ans