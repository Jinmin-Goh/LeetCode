# Problem No.: 678
# Solver:      Jinmin Goh
# Date:        20200417
# URL: https://leetcode.com/problems/valid-parenthesis-string/

import sys

# good solution link: https://leetcode.com/problems/valid-parenthesis-string/discuss/107570/JavaC%2B%2BPython-One-Pass-Count-the-Open-Parenthesis
# greedy algorithm
# time: O(n) / space: O(1)
class Solution:
    def checkValidString(self, s: str) -> bool:
        minCnt = 0
        maxCnt = 0
        for i in s:
            if i == "*":
                maxCnt += 1
                minCnt = max(minCnt - 1, 0)
            elif i == "(":
                maxCnt += 1
                minCnt += 1
            elif i == ")":
                maxCnt -= 1
                minCnt = max(minCnt - 1, 0)
            if maxCnt < 0:
                return False
        if minCnt == 0:
            return True
        else:
            return False