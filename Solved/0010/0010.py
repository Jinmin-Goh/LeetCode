# Problem No.: 10
# Solver:      Jinmin Goh
# Date:        20191204
# URL: 

import sys

class Solution(object):
    def isMatch(self, s, p):
        p1 = len(s) - 1
        p2 = len(p) - 1
        if p == ".*":
            return True
        while p1 >= 0 and p2 >= 0:
            # in case '.'
            if p[p2] == '.':
                p1 -= 1
                p2 -= 1
            # in case ".*"
            elif p2 > 0 and p[p2] == '*' and p[p2 - 1] == '.':
                while p1 >= 0:
                    if self.isMatch(s[0:p1 + 1], p[0:p2 - 1]):
                        return True
                    p1 -= 1
            # in case "?*"
            elif p2 > 0 and p[p2] == '*':
                if s[p1] != p[p2 - 1]:
                    p2 -= 2
                else:
                    while p1 >= 0 and s[p1] == p[p2 - 1]:
                        if self.isMatch(s[0:p1 + 1], p[0:p2 - 1]):
                            return True
                        p1 -= 1
                    #p2 -= 2
            # in simple matching case
            elif s[p1] == p[p2]:
                p1 -= 1
                p2 -= 1
            # none of above
            else:
                return False
        if p1 >= 0:
            return False
        if p2 >= 0:
            while p2 > 0 and p[p2] == '*':
                p2 -= 2
        if p2 >= 0:
            return False
        else:
            return True

        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        