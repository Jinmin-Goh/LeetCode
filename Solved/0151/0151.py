# Problem No.: 151
# Solver:      Jinmin Goh
# Date:        20200717
# URL: https://leetcode.com/problems/reverse-words-in-a-string/

import sys

class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split()
        ans = ""
        for i in reversed(sList):
            ans += i + " "
        return ans[:-1]