# Problem No.: 28
# Solver:      Jinmin Goh
# Date:        20191211
# URL: https://leetcode.com/problems/implement-strstr/

import sys

class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if not haystack:
            return -1
        if len(haystack) == len(needle) and haystack != needle:
            return -1
        if len(haystack) < len(needle):
            return -1
        p1 = 0
        p2 = p1
        while p1 < len(haystack):
            while p1 < len(haystack) and haystack[p1] != needle[0]:
                p1 += 1
            p2 = p1
            while p2 < len (haystack) and (p2 - p1) < len(needle) and haystack[p2] == needle[p2 - p1]:
                p2 += 1
            if (p2 - p1) == len(needle):
                return p1
            p1 += 1
        return -1
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        