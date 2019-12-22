# Problem No.: 60
# Solver:      Jinmin Goh
# Date:        20191222
# URL: https://leetcode.com/problems/permutation-sequence/

import sys

import math
class Solution(object):
    def getPermutation(self, n, k):
        k -= 1
        temp = [i for i in range(1,n+1)]
        ans = ""
        while temp:
            ans += str(temp[k // math.factorial(n - 1)])
            temp.pop(k // math.factorial(n - 1))
            k = k % math.factorial(n - 1)
            n -= 1
        return ans
            
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        