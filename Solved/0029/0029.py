# Problem No.: 29
# Solver:      Jinmin Goh
# Date:        20191212
# URL: https://leetcode.com/problems/divide-two-integers/

import sys

# good solution link: https://leetcode.com/problems/divide-two-integers/discuss/13403/Clear-python-code

class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == -(2 ** 31) and divisor == -1:
            return 2 ** 31 - 1
        ans = 0
        if dividend == 0:
            return 0
        posFlag = True
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            posFlag = False
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        while dividend >= divisor:
            temp = divisor
            count = 1
            while dividend >= temp:
                dividend -= temp
                ans += count
                temp <<= 1
                count <<= 1
        if posFlag:
            return ans
        else:
            return -ans
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        