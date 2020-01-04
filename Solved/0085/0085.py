# Problem No.: 85
# Solver:      Jinmin Goh
# Date:        20200104
# URL: https://leetcode.com/problems/maximal-rectangle/

import sys

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        nrow = len(matrix)
        ncol = len(matrix[0])
        height = [0] * (ncol + 1)
        ans = 0
        for row in matrix:
            for i in range(ncol):
                if row[i] == "1":
                    height[i] += 1
                else:
                    height[i] = 0
            stack = [-1]
            for i in range(ncol + 1):
                while height[i] < height[stack[len(stack) - 1]]:
                    h_val = height[stack.pop()]
                    w_val = i - stack[len(stack) - 1] - 1
                    ans = max(ans, h_val * w_val)
                stack.append(i)
        return ans