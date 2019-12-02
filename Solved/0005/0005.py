# Problem No.: 1
# Solver:      Jinmin Goh
# Date:        20191202
# URL: https://leetcode.com/problems/longest-palindromic-substring/

import sys

class Solution(object):
    def longestPalindrome(self, s):
        p1 = 0
        p2 = 0
        ans = ""
        for i in range(len(s)):
            p1 = i
            p2 = i
            while p1 >= 0 and p2 < len(s):
                if s[p1] != s[p2]:
                    break
                if len(ans) < len(s[p1:p2+1]):
                        ans = s[p1:p2+1]
                p1 -= 1
                p2 += 1
        for i in range(len(s) - 1):
            p1 = i
            p2 = i + 1
            while p1 >= 0 and p2 < len(s):
                if s[p1] != s[p2]:
                    break
                if len(ans) < len(s[p1:p2+1]):
                        ans = s[p1:p2+1]
                p1 -= 1
                p2 += 1
        return ans
        """
        :type s: str
        :rtype: str
        """