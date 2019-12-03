# Problem No.: 8
# Solver:      Jinmin Goh
# Date:        20191203
# URL: https://leetcode.com/problems/string-to-integer-atoi/

import sys

class Solution(object):
    def myAtoi(self, str):
        p = 0
        ans = ''
        # find first non-whitespace
        if str == "":
            return 0
        while p < len(str) and str[p] == ' ':
            p += 1
        
        if p < len(str) and (str[p] == '-' or str[p] == '+'):
            ans += str[p]
            p += 1
        while p < len(str):
            try:
                int(str[p])
                ans += str[p]
                p += 1
            except ValueError:
                break
        if ans == '-' or ans == '' or ans == '+':
            return 0
        elif int(ans) > (2 ** 31 - 1):
            return 2 ** 31 - 1
        elif int(ans) < -(2 ** 31):
            return -(2 ** 31)
        else:
            return int(ans)
        """
        :type str: str
        :rtype: int
        """
        