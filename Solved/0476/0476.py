# Problem No.: 476
# Solver:      Jinmin Goh
# Date:        20200504
# URL: https://leetcode.com/problems/number-complement/

import sys

class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        cnt = 0
        while num > 0:
            if not(num % 2):
                ans +=  2 ** cnt
            cnt += 1
            num >>= 1
        return ans