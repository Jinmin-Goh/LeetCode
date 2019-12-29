# Problem No.: 73
# Solver:      Jinmin Goh
# Date:        20191229
# URL: https://leetcode.com/problems/set-matrix-zeroes/

import sys

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        row_set = set()
        col_set = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
        zero_row = [0] * len(matrix[0])
        for i in row_set:
            matrix[i] = zero_row
        for i in col_set:
            for j in range(len(matrix)):
                matrix[j][i] = 0
        """
        Do not return anything, modify matrix in-place instead.
        """
        
"""
# O(1) memory solution
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    self.zeroFunc(i, j, matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "z":
                    matrix[i][j] = 0
        
    def zeroFunc(self, i: int, j: int, matrix: List[List[int]]) -> None:
        for row in range(len(matrix)):
            if matrix[row][j] != 0:
                matrix[row][j] = "z"
        for col in range(len(matrix[0])):
            if matrix[i][col] != 0:
                matrix[i][col] = "z"

        Do not return anything, modify matrix in-place instead.
        
"""