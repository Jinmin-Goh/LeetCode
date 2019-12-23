# Problem No.: 63
# Solver:      Jinmin Goh
# Date:        20191223
# URL: https://leetcode.com/problems/unique-paths-ii/

import sys

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        dp_table = []
        nrow = len(obstacleGrid)
        ncol = len(obstacleGrid[0])
        for i in range(nrow):
            dp_table.append([0] * ncol)
        if obstacleGrid[0][0] == 1:
            return 0
        dp_table[0][0] = 1
        for i in range(ncol):
            if obstacleGrid[0][i] == 1:
                break
            dp_table[0][i] = 1
        for i in range(nrow):
            if obstacleGrid[i][0] == 1:
                break
            dp_table[i][0] = 1
        if nrow == 1 or ncol == 1:
            return dp_table[nrow - 1][ncol - 1]
        for i in range(1, nrow):
            for j in range(1, ncol):
                if obstacleGrid[i][j] == 1:
                    continue
                dp_table[i][j] = dp_table[i - 1][j] + dp_table[i][j - 1]
        return dp_table[nrow - 1][ncol - 1]
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        