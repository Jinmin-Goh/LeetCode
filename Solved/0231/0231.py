# Problem No.: 231
# Solver:      Jinmin Goh
# Date:        20200608
# URL: https://leetcode.com/problems/power-of-two/

import sys

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        while n > 1:
            if n % 2:
                return False
            n = n // 2
        return True