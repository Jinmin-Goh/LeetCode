# Problem No.: 1009
# Solver:      Jinmin Goh
# Date:        20200505
# URL: https://leetcode.com/problems/complement-of-base-10-integer/

import sys

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        ans = 0
        cnt = 0
        while N > 0:
            if not(N % 2):
                ans +=  2 ** cnt
            cnt += 1
            N >>= 1
        return ans