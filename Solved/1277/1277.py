# Problem No.: 1277
# Solver:      Jinmin Goh
# Date:        20200522
# URL: https://leetcode.com/problems/count-square-submatrices-with-all-ones/

import sys

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        maxSize = min(len(matrix), len(matrix[0]))
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    ans += 1
        size = 2
        while size <= maxSize:
            for i in range(size - 1, len(matrix)):
                for j in range(size - 1, len(matrix[0])):
                    if matrix[i][j - 1] >= size - 1 and matrix[i - 1][j - 1] >= size - 1 and matrix[i - 1][j] >= size - 1 and matrix[i][j] == size - 1:
                        matrix[i][j] = size
                        ans += 1
            size += 1
            #print(matrix)
        return ans
                    
                        