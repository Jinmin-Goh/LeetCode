# Problem No.: 166
# Solver:      Jinmin Goh
# Date:        20200303
# URL: https://leetcode.com/problems/fraction-to-recurring-decimal/

import sys

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        ans = ""
        if numerator * denominator < 0:
            ans += "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        if numerator >= denominator:
            ans += str(numerator // denominator)
            numerator %= denominator
            if numerator == 0:
                return ans
            else:
                ans += "."
        else:
            ans += "0."
        underList = []
        underSet = set()
        tempStr = ""
        normalStr = ""
        repeatStr = ""
        while numerator != 0:
            #print(numerator, tempStr, underList)
            if numerator in underSet:
                repeatStr = tempStr[underList.index(numerator):]
                normalStr = tempStr[:underList.index(numerator)]
                break
            else:
                underList.append(numerator)
                underSet.add(numerator)
            numerator *= 10
            if numerator >= denominator:
                tempStr += str(numerator // denominator)
                numerator %= denominator
            else:
                tempStr += "0"
        if repeatStr:
            ans += normalStr
            ans += "(" + repeatStr + ")"
        else:
            ans += tempStr
        return ans
