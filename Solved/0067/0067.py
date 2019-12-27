# Problem No.: 67
# Solver:      Jinmin Goh
# Date:        20191226
# URL: https://leetcode.com/problems/add-binary/

import sys

class Solution(object):
    def addBinary(self, a, b):
        numA = 0
        numB = 0
        temp = 1
        for i in reversed(range(len(a))):
            if a[i] == '1':
                numA += temp
            temp <<= 1
        temp = 1
        for i in reversed(range(len(b))):
            if b[i] == '1':
                numB += temp
            temp <<= 1
        temp_ans = numA + numB
        if not temp_ans:
            return "0"
        ans = ""
        while temp_ans:
            ans = str(temp_ans % 2) + ans
            temp_ans >>= 1
        return ans
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        