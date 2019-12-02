# Problem No.: 6
# Solver:      Jinmin Goh
# Date:        20191203
# URL: https://leetcode.com/problems/zigzag-conversion/submissions/

import sys

class Solution(object):
    def convert(self, s, numRows):
        if len(s) <= 2 or numRows == 1:
            return s
        ans = ""
        for i in range(numRows):
            j = i
            if j == 0 or j == numRows - 1:
                while j < len(s):
                    ans = ans + s[j]
                    j += 2 * (numRows - 1)
            else:
                flag = False
                while j < len(s):
                    ans = ans + s[j]
                    if(flag):
                        j = j + 2 * i
                        flag = False
                    else:
                        j = j + 2 * (numRows-1-i)
                        flag = True
        return ans
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        