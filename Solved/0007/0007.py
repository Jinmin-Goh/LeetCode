# Problem No.: 7
# Solver:      Jinmin Goh
# Date:        20191203
# URL: https://leetcode.com/problems/reverse-integer/

import sys

class Solution(object):
    def reverse(self, x):
        if x == 0 or x == -(2 ** 31):
            return 0
        ans = ""
        if x < 0:
            ans += "-"
        temp = str(abs(x))
        for i in range(len(temp)):
            ans += temp[len(temp) - 1 - i]
        if int(ans) > (2 ** 31 - 1) or int(ans) < -(2 ** 31):
            return 0
        else:
            return int(ans)
        
        """
        :type x: int
        :rtype: int
        """
        