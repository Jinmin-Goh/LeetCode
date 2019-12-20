# Problem No.: 48
# Solver:      Jinmin Goh
# Date:        20191220
# URL: https://leetcode.com/problems/rotate-image/

import sys

class Solution(object):
    def rotate(self, matrix):
        if matrix == [[1]]:
            return
        length = len(matrix)
        for i in range(length // 2):
            for j in range(i,length - i - 1):
                temp1 = matrix[j][length - i - 1]
                matrix[j][length - i - 1] = matrix[i][j]
                temp2 = matrix[length - i - 1][length - j - 1]
                matrix[length - i - 1][length - j - 1] = temp1
                temp1 = matrix[length - j - 1][i]
                matrix[length - j - 1][i] = temp2
                matrix[i][j] = temp1
                
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        