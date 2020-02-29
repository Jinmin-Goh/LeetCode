# Problem No.: 647
# Solver:      Jinmin Goh
# Date:        20200229
# URL: https://leetcode.com/problems/palindromic-substrings/

import sys

class Solution:
    def countSubstrings(self, s: str) -> int:
        # odd palindrome
        ans = 0
        for i in range(len(s)):
            index = 0
            while i - index >= 0 and i + index < len(s):
                if s[i - index] == s[i + index]:
                    ans += 1
                    index += 1
                else:
                    break
        # even palindrome
        for i in range(len(s) - 1):
            index = 0
            while i - index >= 0 and i + 1 + index < len(s):
                if s[i - index] == s[i + 1 + index]:
                    ans += 1
                    index += 1
                else:
                    break
        return ans