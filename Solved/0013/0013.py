# Problem No.: 13
# Solver:      Jinmin Goh
# Date:        20191205
# URL: https://leetcode.com/problems/roman-to-integer/

import sys

class Solution(object):
    def romanToInt(self, s):
        ans = 0
        i = 0
        while i < len(s) and s[i] == 'M':
            ans += 1000
            i += 1
        # over 100 area
        if i < len(s) and s[i:i+2] == "CM":
            ans += 900
            i += 2
        if i < len(s) and s[i:i+2] == "CD":
            ans += 400
            i += 2
        if i < len(s) and s[i] == 'D':
            ans += 500
            i += 1
        while i < len(s) and s[i] == 'C':
            ans += 100
            i += 1
        # over 10 area
        if i < len(s) and s[i:i+2] == "XC":
            ans += 90
            i += 2
        if i < len(s) and s[i:i+2] == "XL":
            ans += 40
            i += 2
        if i < len(s) and s[i] == 'L':
            ans += 50
            i += 1
        while i < len(s) and s[i] == 'X':
            ans += 10
            i += 1
        # over 1 area
        if i < len(s) and s[i:i+2] == "IX":
            ans += 9
            i += 2
        if i < len(s) and s[i:i+2] == "IV":
            ans += 4
            i += 2
        if i < len(s) and s[i] == 'V':
            ans += 5
            i += 1
        while i < len(s) and s[i] == 'I':
            ans += 1
            i += 1
        return ans
        """
        :type s: str
        :rtype: int
        """
        