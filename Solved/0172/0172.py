# Problem No.: 172
# Solver:      Jinmin Goh
# Date:        20200304
# URL: https://leetcode.com/problems/factorial-trailing-zeroes/

import sys

class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        divider = 5
        while n >= divider:
            ans += n // divider
            divider *= 5
        return ans