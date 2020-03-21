# Problem No.: 329
# Solver:      Jinmin Goh
# Date:        20200322
# URL: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

import sys

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.dpTable = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.dpTable[i][j] == 0:
                    self.DFS(matrix, i, j)
        ans = 0
        for i in self.dpTable:
            ans = max(ans, max(i))
        return ans
        
    def DFS(self, matrix: List[List[int]], i: int, j: int) -> bool:
        #print(self.dpTable, i, j)
        if self.dpTable[i][j] == 1:
            return True
        if self.dpTable[i][j] != 0:
            return True
        temp = matrix[i][j]
        matrix[i][j] = "."
        temp1 = 0
        temp2 = 0
        temp3 = 0
        temp4 = 0
        if i < len(matrix) - 1 and matrix[i + 1][j] != "." and temp > matrix[i + 1][j]:
            if self.DFS(matrix, i + 1, j):
                temp1 = self.dpTable[i + 1][j]
        if i > 0 and matrix[i - 1][j] != "." and temp > matrix[i - 1][j]:
            if self.DFS(matrix, i - 1, j):
                temp2 = self.dpTable[i - 1][j]
        if j < len(matrix[0]) - 1 and matrix[i][j + 1] != "." and temp > matrix[i][j + 1]:
            if self.DFS(matrix, i, j + 1):
                temp3 = self.dpTable[i][j + 1]
        if j > 0 and matrix[i][j - 1] != "." and temp > matrix[i][j - 1]:
            if self.DFS(matrix, i, j - 1):
                temp4 = self.dpTable[i][j - 1]
        if max(temp1, temp2, temp3, temp4) == 0:
            self.dpTable[i][j] = 1
        else:
            self.dpTable[i][j] = max(temp1, temp2, temp3, temp4) + 1
        matrix[i][j] = temp
        return True
        