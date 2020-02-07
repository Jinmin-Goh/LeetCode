# Problem No.: 221
# Solver:      Jinmin Goh
# Date:        20200207
# URL: https://leetcode.com/problems/maximal-square/

import sys

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        dp_matrix = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix) + 1)]
        maxVal = 0
        for i in range(1, len(dp_matrix)):
            for j in range(1, len(dp_matrix[0])):
                if matrix[i - 1][j - 1] == "1":
                    dp_matrix[i][j] = min(dp_matrix[i - 1][j], dp_matrix[i][j - 1], dp_matrix[i - 1][j - 1]) + 1
                    maxVal = max(maxVal, dp_matrix[i][j])
        return maxVal ** 2

        """
        square will be like:
        1 1 1 1 1 
        1 2 2 2 2
        1 2 3 3 3
        1 2 3 4 4
        1 2 3 4 5
        so we need to check only left/up/diagonal member
        """