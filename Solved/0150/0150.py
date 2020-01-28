# Problem No.: 150
# Solver:      Jinmin Goh
# Date:        20200128
# URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/

import sys

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            try:
                int(i)
                stack.append(int(i))
            except ValueError:
                num1 = stack.pop()
                num2 = stack.pop()
                if i == "+":
                    stack.append(num2 + num1)
                elif i == "-":
                    stack.append(num2 - num1)
                elif i == "*":
                    stack.append(num2 * num1)
                elif i == "/":
                    stack.append(int(num2 / num1))
        return stack.pop()