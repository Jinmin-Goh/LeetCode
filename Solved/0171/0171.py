# Problem No.: 171
# Solver:      Jinmin Goh
# Date:        20200303
# URL: https://leetcode.com/problems/excel-sheet-column-number/

import sys

class Solution:
    def titleToNumber(self, s: str) -> int:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = 0
        for i in range(len(s)):
            ans += (alphabet.index(s[-i - 1]) + 1) * (26 ** i)
        return ans