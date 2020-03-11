# Problem No.: 227
# Solver:      Jinmin Goh
# Date:        20200311
# URL: https://leetcode.com/problems/basic-calculator-ii/

import sys

class Solution:
    def calculate(self, s: str) -> int:
        calcList = []
        temp = ""
        for i in s:
            if i == " ":
                continue
            elif i in ["+", "-", "/", "*"]:
                calcList.append(int(temp))
                temp = ""
                calcList.append(i)
            else:
                temp += i
        if temp:
            calcList.append(int(temp))
        i = 0
        while i < len(calcList):
            if calcList[i] in ["+", "-"]:
                i += 1
                continue
            elif calcList[i] == "*":
                calcList[i - 1] = calcList[i - 1] * calcList[i + 1]
                calcList.pop(i)
                calcList.pop(i)
            elif calcList[i] == "/":
                calcList[i - 1] = calcList[i - 1] // calcList[i + 1]
                calcList.pop(i)
                calcList.pop(i)
            else:
                i += 1
        i = 0
        while i < len(calcList):
            if calcList[i] == "+":
                calcList[i - 1] = calcList[i - 1] + calcList[i + 1]
                calcList.pop(i)
                calcList.pop(i)
            elif calcList[i] == "-":
                calcList[i - 1] = calcList[i - 1] - calcList[i + 1]
                calcList.pop(i)
                calcList.pop(i)
            else:
                i += 1
        return calcList[0]