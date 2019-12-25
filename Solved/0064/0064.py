# Problem No.: 64
# Solver:      Jinmin Goh
# Date:        20191224
# URL: https://leetcode.com/problems/minimum-path-sum/

import sys

class Solution(object):
    def minPathSum(self, grid):
        nrow = len(grid)
        ncol = len(grid[0])
        dp_table = [[0] * len(grid[0]) for i in range(len(grid))]
        dp_table[0][0] = grid[0][0]
        for i in range(1, ncol):
            dp_table[0][i] = grid[0][i] + dp_table[0][i - 1]
        for i in range(1, nrow):
            dp_table[i][0] = grid[i][0] + dp_table[i - 1][0]
        for i in range(1, nrow):
            for j in range(1, ncol):
                dp_table[i][j] = min(dp_table[i - 1][j], dp_table[i][j - 1]) + grid[i][j]
        return dp_table[nrow - 1][ncol - 1]
        
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        