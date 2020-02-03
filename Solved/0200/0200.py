# Problem No.: 200
# Solver:      Jinmin Goh
# Date:        20200203
# URL: https://leetcode.com/problems/number-of-islands/

import sys

# BFS solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.bfs(grid, i, j)
                    ans += 1
        return ans
        
    def bfs(self, grid: List[List[str]], i: int, j: int) -> None:
        if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0:
            return
        if grid[i][j] == "1":
            grid[i][j] = "0"
            self.bfs(grid, i + 1, j)
            self.bfs(grid, i, j + 1)
            self.bfs(grid, i - 1, j)
            self.bfs(grid, i, j - 1)
        