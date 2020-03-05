# Problem No.: 191
# Solver:      Jinmin Goh
# Date:        20200305
# URL: https://leetcode.com/problems/number-of-1-bits/

import sys

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n % 2
            n >>= 1
        return ans