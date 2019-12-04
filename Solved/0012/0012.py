# Problem No.: 12
# Solver:      Jinmin Goh
# Date:        20191204
# URL: https://leetcode.com/problems/integer-to-roman/submissions/

import sys

class Solution(object):
    def intToRoman(self, num):
        ans = ""
        while num >= 1000:
            ans += 'M'
            num -= 1000
        # over 100 area
        while num >= 900:
            ans += "CM"
            num -= 900
        if num >= 500:
            ans += 'D'
            while num >= 600:
                ans += 'C'
                num -= 100
            num -= 500
        while num >= 400:
            ans += "CD"
            num -= 400
        while num >= 100:
            ans += 'C'
            num -= 100
        # over 10 area
        while num >= 90:
            ans += "XC"
            num -= 90
        if num >= 50:
            ans += 'L'
            while num >= 60:
                ans += 'X'
                num -= 10
            num -= 50
        while num >= 40:
            ans += "XL"
            num -= 40
        while num >= 10:
            ans += 'X'
            num -= 10
        # over 1 area
        while num >= 9:
            ans += "IX"
            num -= 9
        if num >= 5:
            ans += 'V'
            while num >= 6:
                ans += 'I'
                num -= 1
            num -= 5
        while num >= 4:
            ans += "IV"
            num -= 4
        while num >= 1:
            ans += 'I'
            num -= 1
        return ans
        """
        :type num: int
        :rtype: str
        """
        