# Problem No.: 54
# Solver:      Jinmin Goh
# Date:        20191221
# URL: https://leetcode.com/problems/spiral-matrix/

import sys

class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        ans = []
        nrow = len(matrix)
        ncol = len(matrix[0])
        if nrow == 1:
            return matrix[0]
        if ncol == 1:
            for i in matrix:
                ans += i
            return ans
        if nrow < ncol:
            for i in range(nrow // 2):
                for j in range(i, ncol - i - 1):
                    ans.append(matrix[i][j])
                print(ans)
                for j in range(i, nrow - i - 1):
                    ans.append(matrix[j][ncol - i - 1])
                print(ans)
                for j in range(i, ncol - i - 1):
                    ans.append(matrix[nrow - i - 1][ncol - j - 1])
                print(ans)
                for j in range(i, nrow - i - 1):
                    ans.append(matrix[nrow - j - 1][i])
                print(ans)
        else:
            for i in range(ncol // 2):
                for j in range(i, ncol - i - 1):
                    ans.append(matrix[i][j])
                print(ans)
                for j in range(i, nrow - i - 1):
                    ans.append(matrix[j][ncol - i - 1])
                print(ans)
                for j in range(i, ncol - i - 1):
                    ans.append(matrix[nrow - i - 1][ncol - j - 1])
                print(ans)
                for j in range(i, nrow - i - 1):
                    ans.append(matrix[nrow - j - 1][i])
                print(ans)
        if nrow == ncol and nrow % 2 == 1:
            ans.append(matrix[nrow // 2][nrow // 2])
        elif nrow < ncol and nrow % 2 == 1:
            for i in range(nrow // 2, ncol - nrow // 2):
                ans.append(matrix[nrow // 2][i])
        elif nrow > ncol and ncol % 2 == 1:
            for i in range(ncol // 2, nrow - ncol // 2):
                ans.append(matrix[i][ncol // 2])
            
        return ans
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        