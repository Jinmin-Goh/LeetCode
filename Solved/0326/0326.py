# Problem No.: 326
# Solver:      Jinmin Goh
# Date:        20200319
# URL: https://leetcode.com/problems/power-of-three/

import sys

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 3 == 0 and n > 1:
            n = n // 3
        if n == 1:
            return True
        else:
            return False