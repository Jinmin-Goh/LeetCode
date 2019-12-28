# Problem No.: 69
# Solver:      Jinmin Goh
# Date:        20191228
# URL: https://leetcode.com/problems/sqrtx/

import sys

import math
class Solution:
    def mySqrt(self, x: int) -> int:
        temp_sum = 0
        flag = False
        while True:
            temp = 1
            flag = False
            while (temp_sum + temp) ** 2 <= x:
                flag = True
                temp_sum += temp
                temp <<= 1
            if not flag:
                break
        return temp_sum        
        # one line solution
        #return int(math.sqrt(x))