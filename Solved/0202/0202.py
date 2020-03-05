# Problem No.: 202
# Solver:      Jinmin Goh
# Date:        20200305
# URL: https://leetcode.com/problems/happy-number/

import sys

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0:
            return False
        cntSet = set()
        num = n
        temp = 0
        while num != 1:
            #print(num, temp, cntSet)
            if num in cntSet:
                return False
            cntSet.add(num)
            while num:
                temp += (num % 10) ** 2
                num = num // 10
            num = temp
            temp = 0
        return True