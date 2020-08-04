# Problem No.: 342
# Solver:      Jinmin Goh
# Date:        20200804
# URL: https://leetcode.com/problems/power-of-four/

import sys

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num in [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824]:
            return True
        else:
            return False