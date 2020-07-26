# Problem No.: 258
# Solver:      Jinmin Goh
# Date:        20200726
# URL: https://leetcode.com/problems/add-digits/

import sys

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            temp = 0
            while num:
                temp += num % 10
                num //= 10
            num = temp
        return num