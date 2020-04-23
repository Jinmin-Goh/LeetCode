# Problem No.: 201
# Solver:      Jinmin Goh
# Date:        20200424
# URL: https://leetcode.com/problems/bitwise-and-of-numbers-range/

import sys

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        ans = m
        cnt = 1
        flag = False
        while cnt <= n:
            if cnt >= m:
                flag = True
                ans &= cnt
            cnt <<= 1
        if not flag:
            for i in range(m, n + 1):
                ans &= i
        return ans