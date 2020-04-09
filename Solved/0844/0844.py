# Problem No.: 844
# Solver:      Jinmin Goh
# Date:        20200409
# URL: https://leetcode.com/problems/backspace-string-compare/

import sys

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stackS = []
        for i in S:
            if i == "#":
                if stackS:
                    stackS.pop()
            else:
                stackS.append(i)
        stackT = []
        for i in T:
            if i == "#":
                if stackT:
                    stackT.pop()
            else:
                stackT.append(i)
        if stackS == stackT:
            return True
        else:
            return False