# Problem No.: 59
# Solver:      Jinmin Goh
# Date:        20191222
# URL: https://leetcode.com/problems/spiral-matrix-ii/

import sys

class Solution(object):
    def generateMatrix(self, n):
        if n == 1:
            return [[1]]
        ans = []
        for i in range(n):
            ans.append([0] * n)
        temp = 1
        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                ans[i][j] = temp
                ans[j][n - 1 - i] = temp + n - 1 - 2 * i
                ans[n - 1 - i][n - 1 - j] = temp + 2 * (n - 1 - 2 * i)
                ans[n - 1 - j][i] = temp + 3 * (n - 1 - 2 * i)
                temp += 1
            temp += 3 * (n - 1 - 2 * i)
        if n % 2:
            ans[n // 2][n // 2] = n * n
        return ans 
        """
        :type n: int
        :rtype: List[List[int]]
        """
        