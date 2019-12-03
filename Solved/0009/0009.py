# Problem No.: 9
# Solver:      Jinmin Goh
# Date:        20191203
# URL: https://leetcode.com/problems/palindrome-number/

import sys

class Solution(object):
    def isPalindrome(self, x):
        i = 0
        x = str(x)
        while i in range(len(x) // 2):
            if x[i] != x[len(x) - i - 1]:
                return False
            i += 1
        return True
        """
        :type x: int
        :rtype: bool
        """
        