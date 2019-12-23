# Problem No.: 62
# Solver:      Jinmin Goh
# Date:        20191223
# URL: https://leetcode.com/problems/unique-paths/

import sys

class Solution(object):
    def uniquePaths(self, m, n):
        if m < n:
            m, n = n, m
        ans = 1
        
        for i in range(n - 1):
            ans *= (m + n - 2 - i)
        for i in range(n - 1):
            ans /= i + 1
        return ans
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        