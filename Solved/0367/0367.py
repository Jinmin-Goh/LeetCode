# Problem No.: 367
# Solver:      Jinmin Goh
# Date:        20200510
# URL: https://leetcode.com/problems/valid-perfect-square/

import sys

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        temp = 2 ** 15
        while temp ** 2 > num:
            temp = temp // 2
        for i in range(1, 2 * temp):
            if i ** 2 == num:
                return True
        return False