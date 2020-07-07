# Problem No.: 463
# Solver:      Jinmin Goh
# Date:        20200708
# URL: https://leetcode.com/problems/island-perimeter/

import sys

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        nrow = len(grid)
        ncol = len(grid[0])
        for i in range(nrow):
            for j in range(ncol):
                if i == 0 and grid[i][j] == 1:
                    ans += 1
                if i == nrow - 1 and grid[i][j] == 1:
                    ans += 1
                if i < nrow - 1 and grid[i][j] != grid[i + 1][j]:
                    ans += 1
                if j == 0 and grid[i][j] == 1:
                    ans += 1
                if j == ncol - 1 and grid[i][j] == 1:
                    ans += 1
                if j < ncol - 1 and grid[i][j] != grid[i][j + 1]:
                    ans += 1
        return ans
                    
                    