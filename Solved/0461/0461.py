# Problem No.: 461
# Solver:      Jinmin Goh
# Date:        20200705
# URL: https://leetcode.com/problems/hamming-distance/

import sys

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp = x ^ y
        ans = 0
        while temp:
            if temp % 2:
                ans += 1
            temp >>= 1
        return ans