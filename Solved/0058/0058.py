# Problem No.: 58
# Solver:      Jinmin Goh
# Date:        20191222
# URL: https://leetcode.com/problems/length-of-last-word/

import sys

class Solution(object):
    def lengthOfLastWord(self, s):
        temp = s.split()
        if not temp:
            return 0
        return len(temp[len(temp) - 1])
        """
        :type s: str
        :rtype: int
        """
        