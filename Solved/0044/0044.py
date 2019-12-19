# Problem No.: 0044
# Solver:      Jinmin Goh
# Date:        20191218
# URL: https://leetcode.com/problems/wildcard-matching/

import sys
# good solution vid: https://www.youtube.com/watch?v=3ZDZ-N0EPV0   
class Solution(object):
    def isMatch(self, s, p):
        # dp table represents whether the string(row) matches to pattern(column)
        dp_table = []
        temp = [False] * (len(p) + 1)
        for i in range(len(s) + 1):
            dp_table = dp_table + [temp[:]]
        dp_table[0][0] = True   # "" matches to ""
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                dp_table[0][i] = dp_table[0][i - 1]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp_table[i][j] = dp_table[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp_table[i][j] = dp_table[i - 1][j] or dp_table[i][j - 1]
                else:
                    dp_table[i][j] = False
        return dp_table[len(s)][len(p)]


# right but too slow & not DP used
"""
class Solution(object):
    def isMatch(self, s, p):
        p1 = 0
        p2 = 0
        if p == "*":
            return True
        while p1 < len(s) and p2 < len(p):
            # in case '?'
            if p[p2] == '?':
                p1 += 1
                p2 += 1
            # in case "*"
            elif p[p2] == '*':
                p1_rear = len(s) - 1
                p2_rear = len(p) - 1
                while p[p2_rear] != '*':
                    if p[p2_rear] == '?':
                        p1_rear -= 1
                        p2_rear -= 1
                    elif s[p1_rear] == p[p2_rear]:
                        p1_rear -= 1
                        p2_rear -= 1
                    elif s[p1_rear] != p[p2_rear]:
                        return False
                
                while p2 < len(p) - 1 and p[p2 + 1] == '*':
                    p2 += 1
                while p1 < len(s):
                    if self.isMatch(s[p1:], p[p2 + 1:]):
                        return True
                    p1 += 1
            # in simple matching case
            elif s[p1] == p[p2]:
                p1 += 1
                p2 += 1
            # none of above
            else:
                return False
        if p1 < len(s):
            return False
        if p2 < len(p):
            while p2 < len(p) and p[p2] == '*':
                p2 += 1
        if p2 < len(p):
            return False
        else:
            return True
        :type s: str
        :type p: str
        :rtype: bool
        """
        