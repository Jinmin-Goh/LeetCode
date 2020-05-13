# Problem No.: 402
# Solver:      Jinmin Goh
# Date:        20200513
# URL: https://leetcode.com/problems/remove-k-digits/

import sys

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while stack and stack[-1] > i and k > 0:
                stack.pop()
                k -= 1
            stack.append(i)
        if k > 0:
            stack = stack[:-k]
        ans = ""
        for i in stack:
            ans += i
        ans = ans.lstrip("0")
        if ans:
            return ans
        else:
            return "0"