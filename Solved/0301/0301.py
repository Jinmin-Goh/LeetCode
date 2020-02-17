# Problem No.: 301
# Solver:      Jinmin Goh
# Date:        20200217
# URL: https://leetcode.com/problems/remove-invalid-parentheses/

import sys

# good solution link: https://leetcode.com/problems/remove-invalid-parentheses/discuss/75027/Easy-Short-Concise-and-Fast-Java-DFS-3-ms-solution

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.ans = []
        self.remove(s, 0, 0, "(", ")")
        return self.ans
        
        
    def remove(self, s: str, iVal: int, jVal: int, left: str, right: str) -> None:
        leftVal, rightVal = 0, 0
        for i in range(iVal, len(s)):
            if s[i] == left:
                leftVal += 1
            elif s[i] == right:
                rightVal += 1
            # if there is extra ")"
            if rightVal > leftVal:
                for j in range(jVal, i + 1):
                    if s[j] == right and (j == jVal or s[j - 1] != right):
                        self.remove(s[:j] + s[j + 1:], i, j, left, right)
                return
        # no more extra ")", reverse the string and do it again
        revStr = ""
        for i in reversed(range(len(s))):
            revStr += s[i]
        if left == "(":
            self.remove(revStr, 0, 0, ")", "(")
        else:
            self.ans.append(revStr)