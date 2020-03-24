# Problem No.: 344
# Solver:      Jinmin Goh
# Date:        20200324
# URL: https://leetcode.com/problems/reverse-string/

import sys

class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]