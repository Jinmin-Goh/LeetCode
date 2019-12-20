# Problem No.: 50
# Solver:      Jinmin Goh
# Date:        20191220
# URL: https://leetcode.com/problems/powx-n/

import sys

class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1.0
        if n == 1:
            return x
        ans = 1.0
        # in case of n is positive
        if n > 0:
            while n > 0:
                i = 1
                temp = x
                while i <= n:
                    ans *= temp
                    temp *= temp
                    n -= i
                    i <<= 1
        else:
            n = -n
            while n > 0:
                i = 1
                temp = x
                while i <= n:
                    ans /= temp
                    temp *= temp
                    n -= i
                    i <<= 1

        return ans
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        