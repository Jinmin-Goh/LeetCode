# Problem No.: 66
# Solver:      Jinmin Goh
# Date:        20191226
# URL: https://leetcode.com/problems/plus-one/

import sys

class Solution(object):
    def plusOne(self, digits):
        i = len(digits) - 1
        while i >= 0:
            temp = digits[i] + 1
            digits[i] = temp % 10
            if temp >= 10:
                if i == 0:
                    digits = [1] + digits
                else:
                    i -= 1
                    continue
            break
        return digits
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        