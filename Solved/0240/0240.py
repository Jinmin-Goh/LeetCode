# Problem No.: 240
# Solver:      Jinmin Goh
# Date:        20200211
# URL: https://leetcode.com/problems/search-a-2d-matrix-ii/

import sys

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        for i in matrix:
            if i[0] > target:
                break
            if i[-1] < target:
                continue
            for j in i:
                if j == target:
                    return True
                elif j > target:
                    break            
        return False